"""A sample Celery task module."""

import time

from celery import Celery


app = Celery("sample_task", broker="redis://redis.server:6379", backend="redis://redis.server:6379/1")


@app.task
def add(x: int = 0, y: int = 0) -> int:
    """A sample Celery task that adds two numbers after a delay."""
    time.sleep(5)
    print(x + y)
    return x + y
