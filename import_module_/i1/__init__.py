

from importlib import import_module



from importlib import import_module
from importlib import __import__

a = import_module(".i2" ,"")

c = getattr(a, "A")
print(c)
c.run()