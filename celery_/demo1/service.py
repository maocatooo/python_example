from celery import Celery
import time
app = Celery('service', backend='redis://0.0.0.0:6379/0',
             broker='redis://0.0.0.0:6379/0')  # 配置好celery的backend和broker


@app.task  # 普通函数装饰为 celery task
def add(x, y):
    time.sleep(2)
    return x + y


