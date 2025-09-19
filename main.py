import random

from celery_task import add

if __name__ == "__main__":
    result: int = add.delay(random.randint(1, 100), random.randint(1, 100))
