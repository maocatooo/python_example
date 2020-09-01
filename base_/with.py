import redis
import threading
pool = redis.ConnectionPool(
    host='0.0.0.0',
    port=6379,
    db=13,
    decode_responses=True)
import time
REDIS = redis.Redis(connection_pool=pool)


class A(object):

    def __init__(self, id=None):
        if REDIS.incr(id) != 1:
            print('over')
            return
        self.id = id
        print('初始化')

    def __enter__(self):
        print('开始')

    def __exit__(self, *args, **kwargs):
        print('结束')
        if hasattr(self, 'id'):
            REDIS.delete(self.id)

def ad():
    with A(id='abc') as a:
        time.sleep(0.1)
        print('中间')
        return


import threading
task_list = []
for one in range(20):
    t = threading.Thread(target=ad)
    task_list.append(t)

for one in task_list:
    one.start()

for one in task_list:
    one.join()



