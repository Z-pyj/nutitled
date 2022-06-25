import pika
import requests
import pickle
# dump和dumps的区别：
# dump是将对象序列化并保存到文件中
# dumps是将对象序列化

# load和loads的区别：
# load将序列化字符串从文件读取并反序列化
# loads将序列化字符串反序列化
MAX_PRIORITY = 100
TOTAL = 100
QUEUE_NAME = 'scrape_queue'
# 连接mabbitMq服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 频道对象
channel = connection.channel()
# 声明一个队列
# TODO:声明队列时指定durable为True,开启持久化存储
channel.queue_declare(queue=QUEUE_NAME, durable=True)
# 添加消息,随去随用
for i in range(1, TOTAL + 1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ),
                          body=pickle.dumps(request))
    print(f'Put request of {url}')
