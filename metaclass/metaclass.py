import six


class A(type):
    
    def __new__(mcs, name: str, bases, attrs):
        print(name)
        print(bases)
        print(attrs)
        print(attrs.get('Meta'))
        klass = super(A, mcs).__new__(mcs, name, bases, attrs)
        print(klass)
        return klass


class B(object):
    pass


class C(six.with_metaclass(A, B)):
    pass


class D(C):
    a = 1

    class Meta:
        pass


class A:
    pass


class B(A):
    pass


class cc(B):
    pass


print(issubclass(cc, A))  # 判断没有实例化的类是不是其它类的子类
print(isinstance(cc(), (A,)))  # 判断实例化的类是不是其它类的子类
