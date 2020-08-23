#!/usr/bin/env python
import os
import time
import pika
import random

time.sleep(25)

connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['HOST_IP'], 5672))
channel = connection.channel()
channel.queue_declare(queue='lanit')

for i in range(10):
	r = random.randint(1, 10)
	if 1989 % (r+i) == 0:
		msg = str(r)+str(i)
		channel.basic_publish(exchange='', routing_key='lanit', body=msg)
		print(" [x] Sent {}".format(msg))
		time.sleep(1)
channel.basic_publish(exchange='', routing_key='lanit', body='')
connection.close()
