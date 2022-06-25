import pika

QUEUE_NAME = 'scrape'
# 连接mabbitMq服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 频道对象
channel = connection.channel()
# 声明一个队列
channel.queue_declare(queue=QUEUE_NAME)
# 添加消息,随去随用
while True:
    # TODO:使用input方法来获取生产者数据，输入的内容会自动放到队列中

    data = input()
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          body=data)
    print(f'PUT {data}')


