import pika

QUEUE_NAME = 'scrape'
# 连接mabbitMq服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 频道对象
channel = connection.channel()
# 声明一个队列
channel.queue_declare(queue=QUEUE_NAME)
# 添加消息
channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=b'Hello World')
