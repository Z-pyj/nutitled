import aiohttp
import asyncio

# TODO:aiohttp是一个基于asyncio的异步网络模块，类似request，但他是异步的
# 基本实例
'''
1. 每个方法前都是async修饰
2. with open 前加async修饰，代表声明一个支持异步的上下文管理器
3. 返回协程对象的操作，前面需要加上await 
'''


async def fatch(session, url):
    async with session.get(url) as response:
        return await  response.text(), response.status


# # 基本实例
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html, status = await fatch(session, 'https://cuiqingcai.com')
#         print(f'html:{html[:100]}...')
#         print(f'status:{status}')

# # url参数设置
# async def main():
#     params = {'name': 'zw', 'age': 33}
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.httpbin.org/get', params=params) as response:
#             print(await response.text())

# # post请求,对于请求头中content-type为application/x-www-form-urlencoded使用data参数
# async def main():
#     data = {'name': 'zw', 'age': 33}
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.httpbin.org/get', data=data) as response:
#             print(await response.text())

# # post请求,对于请求头中content-type为application/json的使用data参数
# async def main():
#     data = {'name': 'zw', 'age': 33}
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.httpbin.org/get', json=data) as response:
#             print(await response.text())

# # 分别获取响应码，响应头，响应体，响应体二进制内容，响应体json结果
# async def main():
#     data = {'name': 'zw', 'age': 33}
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.httpbin.org/get', json=data) as response:
#             print(response.status)
#             print(response.headers)
#             print(await response.text())
#             print(await response.read())
#             print(await response.json())

# 超时设置
async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    data = {'name': 'zw', 'age': 33}
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://www.httpbin.org/get', json=data) as response:
            print(response.status)
            print(response.headers)
            print(await response.text())
            print(await response.read())
            print(await response.json())
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # asyncio.run(main())
