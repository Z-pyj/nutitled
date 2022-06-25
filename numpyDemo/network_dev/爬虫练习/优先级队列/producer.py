import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape'
# 连接mabbitMq服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 频道对象
channel = connection.channel()
# 声明一个队列
channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-priority': MAX_PRIORITY})
# 添加消息,随去随用
while True:
    # TODO:声明时增加x-max-prioryty属性来实现优先级

    data, priority = input().split()
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          properties=pika.BasicProperties(
                              priority=int(priority)
                          ),
                          body=data)
    print(f'PUT {data}')
