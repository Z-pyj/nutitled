import time
import aiohttp
import asyncio

# TODO:协程实现
start = time.time()

# 协程对象
async def get(url):
    # aiohttp.ClientSession类中的get方法进行请求
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    # await方法后面跟上协程对象
    response = await get(url)
    print('Get response from', url, 'response', response)

# 定义一个task列表
tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# 事件循环
loop = asyncio.get_event_loop()
# 使用asyncio.wait方法执行
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cos time:', end-start)
