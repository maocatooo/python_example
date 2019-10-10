def decorator(func):
    print 'ddd'
    return lambda *args, **kwargs: func(*args, **kwargs)


@decorator
def function(a,b,c=None):
    print a
    print b
    print("hello, decorator")

