import asyncio
import time

'''协程 Future'''
# ----------------------------------------
''' 
demo url : https://thief.one/2018/06/21/1/#more
'''
# async def test1():
#     print("1")
#     print("2")
#
#
# async def test2():
#     print("3")
#     print("4")
# print(test1())
# print(test2())
# a = test1()
# b = test2()

# try:
#     a.send(None) # 可以通过调用 send 方法，执行协程函数
# except StopIteration as e:
#     print(e.value)
#     # 协程函数执行结束时会抛出一个StopIteration 异常，标志着协程函数执行结束，返回值在value中
#
# try:
#     b.send(None) # 可以通过调用 send 方法，执行协程函数
# except StopIteration as e:
#     print(e.value)
# 协程函数执行结束时会抛出一个StopIteration 异常，标志着协程函数执行结束，返回值在value中


# ----------------------------------------
# async def test1():
#     print("1")
#     # await test2()
#     print("2")
#
#
# async def test2():
#     print("3")
#     print("4")
#
#
# # 事件循环方法 自动得执行所有的协程函数
# loop = asyncio.get_event_loop()

# loop.run_until_complete(test1())
# ----------------------------------------


# task任务
#
# import asyncio
# async def test1():
#     print("1")
#     await test2()
#     print("2")
#     asyncio.sleep(2)
#     return "stop"
# async def test2():
#     print("3")
#     print("4")
# loop = asyncio.get_event_loop()
# # 手动将协程包裹成task对象
# task = loop.create_task(test1())
# loop.run_until_complete(task)
# # task = asyncio.ensure_future(test1())
# loop.run_until_complete(task)
# # 获取协程返回的值
# print(task.result())

# async def test(arg):
#     t1 = time.time()
#     b = [i for i in range(10000000)]
#     d = '0'
#     for i in b:
#         d += str(i)
#     return time.time() - t1
#
#
# async def test1(arg):
#     t1 = time.time()
#     a = [i for i in range(1000, 10000000)]
#     d = '0'
#     for i in a:
#         d += str(i)
#     return time.time() - t1
# import time
# t1 = time.time()
# loop = asyncio.get_event_loop()
# task1 = asyncio.ensure_future(test('ok'))
# task2 = asyncio.ensure_future(test1('ok1'))
#
# loop.run_until_complete(asyncio.wait([task1, task2]))
# print(task1.result())
# print(task2.result())
# print(time.time() - t1)

import time
import asyncio
import requests
import functools
url = 'http://127.0.0.1:5000/manager/search/select/data'


async def async_run(url):
    loop = asyncio.get_event_loop()
    try:
        # 利用functools.partial 偏函数 将requests.get封装
        # loop.run_in_executor 创建线程执行耗时函数
        response = await loop.run_in_executor(None, functools.partial(requests.get, url=url, params="", timeout=1))
    except Exception as e:
        print(e)
    else:
        return response.url


def run(url):
    try:
        response = requests.get(url=url, params="", timeout=1)
    except Exception as e:
        print(e)
    else:
        return response.url


t1 = time.time()
tasks = [asyncio.ensure_future(async_run(url)) for i in range(2000)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print('async run: ', time.time() - t1)

t1 = time.time()
[run(url) for i1 in range(2000)]
print('run: ', time.time() - t1)
