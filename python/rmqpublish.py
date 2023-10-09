#Get a file from the command line and publish it to RabbitMQ using the default exchange

import pika
import sys

# Connect to the RabbitMQ server
rmqHost = 'localhost'
rmqUser = 'guest'
rmqPass = 'guest'
rmqVHost = '/'
rmqPort = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmqHost, port=rmqPort, virtual_host=rmqVHost, credentials=pika.PlainCredentials(rmqUser, rmqPass)))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='hello')

# Get the file name from the command line
filename = sys.argv[1]

# Publish the file to the queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=open(filename).read())

# Close the connection
connection.close()
