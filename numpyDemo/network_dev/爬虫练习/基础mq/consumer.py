import pika

QUEUE_NAME = 'scrape'
# 连接mabbitMq服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 频道对象
channel = connection.channel()
# 声明一个队列
channel.queue_declare(queue=QUEUE_NAME)


# 从队列中获取数据
def callback(ch, method, properties, body):
    print(f"GET {body}")


channel.basic_consume(queue='scrape',
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
