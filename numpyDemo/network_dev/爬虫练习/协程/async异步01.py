import asyncio

# TODO:协程基本使用
# async关键字定义方法
async def excute(x):
    print('Number:', x)


# 方法没有被执行，返回一个coroutine协程对象
coroutine = excute(1)
print('Coroutine:', coroutine)
print('After calling excute')
# 使用get_event_loop()方法创建一个事件循环loop
loop = asyncio.get_event_loop()
# run_until_complete方法将协程对象注册到循环loop中，接着启动
loop.run_until_complete(coroutine)
print('After calling loop')
