#RabbitMQ Consumer

import pika
import os
import sys
import ssl

rmqHost = os.environ.get('RMQ_HOST', 'localhost')
rmqUser = os.environ.get('RMQ_USER', 'guest')
rmqPass = os.environ.get('RMQ_PASS', 'guest')
rmqVHost = os.environ.get('RMQ_VHOST', '/')
rmqPort = int(os.environ.get('RMQ_PORT', '5671'))
rmqQueue = os.environ.get('RMQ_QUEUE', 'hello')
rmqExchange = os.environ.get('RMQ_EXCHANGE', '')

cxt = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_options = pika.SSLOptions(context=cxt, server_hostname=rmqHost)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmqHost, port=rmqPort, virtual_host=rmqVHost, credentials=pika.PlainCredentials(rmqUser, rmqPass), ssl_options=ssl_options))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=rmqQueue, durable=True)

# Define a callback function to process the message
def callback(ch, method, properties, body):
    #Print the size of the message
    print(f"Received message of size {len(body)}")

# Subscribe the callback function to the queue
channel.basic_consume(queue=rmqQueue,
                      on_message_callback=callback,
                      auto_ack=True)

# Wait for messages
print('Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
