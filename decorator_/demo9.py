import functools

'''
functools .wraps 装饰器，它的作用就是将 被修饰的函数(wrapped) 的一些属性值赋值给 修饰器函数(wrapper) ，最终让属性的显示更符合我们的直觉
'''
def wrapper(func):
    def inner_function():
        pass
    return inner_function


@wrapper    # = wrapper(func)
def wrapped():
    pass


print(wrapped.__name__)
#inner_function


def wrapper1(func):

    @functools.wraps(func)
    def inner_function():
        pass
    return inner_function


@wrapper1    # = wrapper(func)
def wrapped1():
    pass


print(wrapped1.__name__)
# wrapped1