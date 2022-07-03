import asyncio
import requests

# TODO:回调方法
# async关键字定义方法
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

# 回调方法,返回task结果
def callback(task):
    print('Status:', task.result())


coroutine = request()
# 定义task对象
task = asyncio.ensure_future(coroutine)
# task对象绑定回调对象
task.add_done_callback(callback)
print('Task', task)
# 定义事件循环loop
loop = asyncio.get_event_loop()
# 注册到事件循环中
loop.run_until_complete(task)
print('Task:', task)
# task.result同样可以返回task结果
print('Task:', task.result())

