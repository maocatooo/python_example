
class A1(object):
    def run(self):
        print("run A")


class A(A1):
    pass


class B(A1):

    def run(self):
        print("run B")


class C(A, B):
    pass


C().run()
