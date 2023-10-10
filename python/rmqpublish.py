#Get a file from the command line and publish it to RabbitMQ using the default exchange

import pika
import sys
import ssl

# Connect to the RabbitMQ server
import os

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
channel.queue_declare(queue=rmqQueue)

# Get the file name from the command line
filename = sys.argv[1]

# Publish the file to the queue
channel.basic_publish(exchange=rmqExchange,
                      routing_key='hello',
                      body=open(filename).read())

# Close the connection
connection.close()
