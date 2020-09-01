import os
from threading import Lock
from typing import List

path = os.path.dirname(__file__)


class Rotation(object):
    lock = Lock()
    __letter = list('abcdefghijklmnopqrstuvwxyz')
    __number = list('0123456789')
    __data = __letter + __number
    __max_index = 35

    def __init__(self, r_data: str = None):
        if not r_data:
            self.__generate()
        else:
            self._validate(r_data)
        print(self._r_data)

    def __run(self, val):
        val = val or 'abc'

        ind = [self.__data.index(i) for i in val]
        self.__inc(ind)
        self._r_data = ''.join([self.__data[i] for i in ind])

    @staticmethod
    def __inc(ind: List[int]):
        ind[-1] += 1
        if ind[-1] > Rotation.__max_index:
            ind[-2] += 1
            ind[-1] = 0
        if ind[-2] > Rotation.__max_index:
            ind[-2] = 0
            ind[-3] += 1
        if ind[-3] > Rotation.__max_index:
            ind[0] = ind[1] = ind[2] = 0

    def __generate(self):
        with self.lock:
            rotation_file = os.path.join(path, '.rotation')
            if os.path.isfile(rotation_file):
                with open(rotation_file, 'r') as f:
                    self.__run(f.read())
                with open(rotation_file, 'w') as f:
                    f.write(self._r_data)
            else:
                self._r_data = 'abc'
                with open(rotation_file, 'w') as f:
                    f.write(self._r_data)

    def _validate(self, r_data):
        if len(r_data) == 3:
            for item in r_data:
                if item not in self.__data:
                    break
            else:
                self.__run(r_data)
        raise ValueError('错误的r_data, 必须是3位小写字母,或者数字')

    def __str__(self):
        return self._r_data

    __repl__ = __str__


if __name__ == '__main__':

    import threading
    task_list = []
    for one in range(30):
        t = threading.Thread(target=Rotation)
        task_list.append(t)

    for one in task_list:
        one.start()

    for one in task_list:
        one.join()
