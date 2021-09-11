#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='hello')

body = b'ABRACADABRA!'

channel.basic_publish(exchange='', routing_key='hello', body=body)
print(" [x] Sent %r" % body)
connection.close()
