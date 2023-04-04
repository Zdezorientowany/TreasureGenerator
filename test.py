import queue
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Create a message queue
channel.queue_declare(queue='hello')

# Send messages to the queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Generate')

# Close the connection
connection.close()