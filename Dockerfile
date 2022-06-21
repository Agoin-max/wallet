FROM python:3.8.5
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /src/
  
ADD ./requirements.txt /src/

RUN pip install websocket-client==0.14.0
RUN pip install -r /src/requirements.txt
RUN pip install celery
RUN pip install vine==1.3.0 mysqlclient gunicorn[gevent]
ADD . /src/
CMD gunicorn -w 2 -k gevent -b 0.0.0.0:8080 wallet.wsgi:application
