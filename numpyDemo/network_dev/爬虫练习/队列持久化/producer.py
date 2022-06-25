import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape'
# 连接mabbitMq服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 频道对象
channel = connection.channel()
# 声明一个队列
# TODO:声明队列时指定durable为True,开启持久化存储
channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-priority': MAX_PRIORITY},durable=True)
# 添加消息,随去随用
while True:
    # TODO:同时在添加消息的时候指定basicproperties对象的delivery_mode为2

    data, priority = input().split()
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          properties=pika.BasicProperties(
                              priority=int(priority),
                              delivery_mode=2
                          ),
                          body=data)
    print(f'PUT {data}')
