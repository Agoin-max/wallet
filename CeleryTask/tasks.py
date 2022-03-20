from wallet.celery import app
import logging
from celery import shared_task

logger = logging.getLogger(__name__)


@app.task
def add(x, y):
    logger.info("顺利进行")
    return x + y


@app.task
def print_every_time():
    logger.info("test")
