import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()
channel.queue_declare(queue='tasks')

channel.basic_publish(exchange='', routing_key='tasks', body='this is my task')
print("Daniel send a task")
connection.close()