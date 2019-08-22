l = [1, 3, 4, 5, 6]

print([i for i in map(lambda x: x+1, l)])


def f(x):
    return x+2


print([i for i in map(f, l)])
