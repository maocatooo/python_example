
from typing import Callable
import flask
import redis
import time
pool = redis.ConnectionPool(
    host='127.0.0.1',
    port=6379,
    db=12,
    decode_responses=True)

REDIS = redis.Redis(connection_pool=pool)
app = flask.Flask(__name__)


# 拦截器
class Interceptor(object):

    def __init__(
            self,
            id: str,
            over_func: Callable = None):
        key = f"i:{id}:c"
        if REDIS.incr(key) != 1:
            if over_func:
                over_func(401)
            return
        self.key = key

    def __enter__(self):
        pass

    def __exit__(self, *args, **kwargs):
        print("over1")
        if hasattr(self, 'key'):
            REDIS.delete(self.key)


def ov(fun):
    def d():
        with Interceptor("123", over_func=flask.abort):
            time.sleep(5)
            flask.abort(404)
            res = fun()
        return res
    return d


@app.route("/")
@ov
def index():
    return {"1": "123"}


if __name__ == '__main__':
    app.run(debug=True, port=5001)