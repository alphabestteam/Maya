import pika, sys, os
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='tasks')

    def callback(ch, method, properties, body):
        print (" [x] Received %r" % body)

    channel.basic_consume(queue='tasks', on_message_callback=callback, auto_ack=True)
    print('Shelly is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()