import time
# 这是装饰函数
def timer(func):
    def wrapper(*args, **kw):
        t1=time.time()
        # 这是函数真正执行的地方
        func(*args, **kw)
        t2=time.time()

        # 计算下时长
        cost_time = t2-t1
        print("花费时间：{}秒".format(cost_time))
    return wrapper

@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)

want_sleep(5)