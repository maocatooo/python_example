class MyDict(dict):
    def __getattr__(self, value):
        keyName = value[0].upper() + value[1:]
        print(keyName)
        try:
            return self[keyName]
        except KeyError:
            raise AttributeError("'%s' object has no attribute '%s'" % (
                self.__class__.__name__.split('.')[-1], value))

    def get(self, v, d=None):
        try:
            return self[v]
        except KeyError:
            return d

    def __getattribute__(self, item):
        print(item)
        return


mu = MyDict()

mu['Dd'] = 'asd'

print(mu.get)
print(mu['Dd'])
