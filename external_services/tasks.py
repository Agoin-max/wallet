from wallet.celery import app
import logging

logger = logging.getLogger(__name__)


# 测试用
@app.task
def test():
    logger.info("test")