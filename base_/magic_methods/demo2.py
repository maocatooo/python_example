a = 5
# def fn():
#
#     a = 4
# fn()
# print(a)
class Obj(object):
    global a
    def __init__(self, d):
        a = d
        self.a = a
        print(d)
        print('im init')

    def __new__(cls, *args, **kwargs):
        print('im new')
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        print('im call')

obj = Obj('1')
print(obj.a)
obj()
