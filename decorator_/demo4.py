from functools import wraps

def say_hello(contry):

    def wrapper(func):
        # 中间不能加任何逻辑化的东西， 这里的代码只在加载的时候执行一次 亲自踩过的坑
        @wraps(func)
        def deco(*args, **kwargs):

            # 真正执行函数的地方
            return func(*args, **kwargs)
        return deco
    return wrapper


@say_hello("china")
def xiaoming(asd):
    return (asd)

@say_hello("america")
def jack():
    pass

print(xiaoming(12333))
print('====================')
jack()