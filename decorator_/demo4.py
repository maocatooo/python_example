def say_hello(contry):
    def wrapper(func):
        # 中间不能加任何逻辑化的东西， 这里的代码只在加载的时候执行一次 亲自踩过的坑
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好!")
            elif contry == "america":
                print('hello.')
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)
        return deco(args, kwargs)()
    return wrapper


@say_hello("china")
def xiaoming():
    pass

@say_hello("america")
def jack():
    pass

xiaoming()
print('====================')
jack()