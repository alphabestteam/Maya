import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()
channel.queue_declare(queue='tasks')

channel.basic_publish(exchange='task', routing_key='tasks', body='creating a website that manages tasks')
print("Daniel send a task")
connection.close()