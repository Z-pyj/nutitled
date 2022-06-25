import pika
import pickle
import requests

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape_queue'
# 连接mabbitMq服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 频道对象
channel = connection.channel()
session = requests.Session()


def scrape(request):
    try:
        response = session.send(request.prepare())
        print(f'success scraped {response.url}')
    except request.RequestException:
        print(f'error occurred when scraping {request.url}')


# 从队列中获取数据
while True:
    # TODO:input方法控制消费者何时获取下一个数据，获取方法是basic_get，方法返回要给元组，其中body就是真正的数据

    input()
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True
    )
    if body:
        request = pickle.loads(body)
        print(f'Get {request}')
        scrape(request)
