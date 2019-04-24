import asyncio
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

import asyncio
async def test1():
    print("1")
    await test2()
    print("2")
    asyncio.sleep(2)
    return "stop"
async def test2():
    print("3")
    print("4")
loop = asyncio.get_event_loop()
# 手动将协程包裹成task对象
task = loop.create_task(test1())
loop.run_until_complete(task)
# task = asyncio.ensure_future(test1())
loop.run_until_complete(task)
# 获取协程返回的值
print(task.result())