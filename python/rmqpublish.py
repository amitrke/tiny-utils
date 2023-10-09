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

ssl_options = {
    "ssl_version": ssl.PROTOCOL_TLSv1_2,
    # "ca_certs": "/path/to/ca_certificate.pem",
    # "certfile": "/path/to/client_certificate.pem",
    # "keyfile": "/path/to/client_key.pem",
    "cert_reqs": ssl.CERT_REQUIRED
}

# context = ssl.create_default_context(cafile=ssl_options['ca_certs'])
# ssl_options["context"] = context

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmqHost, port=rmqPort, virtual_host=rmqVHost, credentials=pika.PlainCredentials(rmqUser, rmqPass), ssl=True, ssl_options=ssl_options))
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
