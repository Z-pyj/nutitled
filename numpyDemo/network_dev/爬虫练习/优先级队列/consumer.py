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


# 从队列中获取数据
while True:
    # TODO:input方法控制消费者何时获取下一个数据，获取方法是basic_get，方法返回要给元组，其中body就是真正的数据

    input()
    method_frame, header, body=channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True
    )
    if body:
        print(f'Get {body}')

