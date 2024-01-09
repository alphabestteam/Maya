import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare(queue='tasks', durable=True)
print(' team mates are waiting for messages. To exit press CTRL+C')
def callback(ch, method, properties, body):
    print("team mates Received %r" %body.decode())
    time.sleep(2)
    print("team mates Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='tasks', on_message_callback=callback)
channel.start_consuming()