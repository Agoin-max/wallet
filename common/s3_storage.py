import mimetypes
import boto3
import os
import hashlib
import logging
import io
import uuid
from django.conf import settings

logger = logging.getLogger(__name__)


class Storage:
    def __init__(self):
        self.ak = settings.S3_KEY.get("AWS_ACCESS_AK")
        self.sk = settings.S3_KEY.get("AWS_ACCESS_SK")
        self.region = settings.S3_KEY.get("REGION")
        self.bucket = settings.S3_KEY.get("AWS_STORAGE_BUCKET")
        self.s3 = boto3.resource("s3", aws_access_key_id=self.ak,
                                 aws_secret_access_key=self.sk, region_name=self.region)

    def generate_path(self, filename, t, md5):
        id_ = str(uuid.uuid4())
        return '{t}/{one}/{two}/{uuid}{ext}'.format(
            t=t,
            one=md5[:2],
            two=md5[2:4],
            uuid=id_,
            ext=os.path.splitext(filename.rstrip())[1].lower(),
        )

    def mime_type(self, filename):
        return mimetypes.guess_type(filename)[0] or "application/octet-stream"

    def _upload(self, filename, path, data):
        headers = {'ContentType': '%s; charset=utf-8' % self.mime_type(filename)}
        try:
            self.s3.Bucket(self.bucket).put_object(Key=path, Body=data, **headers)
            size = len(data)
            return size
        except (Exception,) as e:
            logger.error("s3 upload file err: %s" % e)
            return None

    def upload(self, filename, data, ftype="1", md5=""):
        if not md5:
            md5 = hashlib.md5(data).hexdigest()
        path = self.generate_path(filename, ftype, md5)
        size = self._upload(filename, path, data)
        if not size:
            return None
        return {"path": path, "md5": md5, "size": size, "name": filename}

    def upload_file(self, file_path, ftype="1"):
        fh = open(file_path, "rb")
        data = fh.read()
        fh.close()
        md5 = hashlib.md5(data).hexdigest()
        filename = file_path.split("/")[-1]
        return self.upload(filename, data, ftype, md5)

    def upload_file_to_path(self, file_path, up_path):
        fh = open(file_path, "rb")
        data = fh.read()
        fh.close()
        md5 = hashlib.md5(data).hexdigest()
        filename = file_path.split("/")[-1]
        if up_path[0] == "/":
            path = "uptx%s" % up_path
        else:
            path = "uptx/%s" % up_path

        size = self._upload(filename, path, data)
        if not size:
            return None
        return {"path": path, "md5": md5, "size": size, "name": filename}

    def download(self, path):
        try:
            s = io.BytesIO()
            self.s3.Bucket(self.bucket).download_fileobj(path, s)
            return s.getvalue()
        except (Exception,) as e:
            logger.error(">>> s3 download err: %s, %s" % (e, path))
            return None

    def delete(self, path):
        try:
            dic = {"Objects": [{"Key": path}], "Quiet": True}
            self.s3.Bucket(self.bucket).delete_objects(Delete=dic)
        except (Exception,):
            import traceback
            print(traceback.format_exc())
            return False
