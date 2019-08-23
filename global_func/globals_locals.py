a = 1

print(__file__)

def func(c):
    d = 1
    print(globals())
    print(locals())

func(2)