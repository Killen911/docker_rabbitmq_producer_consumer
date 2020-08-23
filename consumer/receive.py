#!/usr/bin/env python
import os
import time
import pika

time.sleep(25)

connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['HOST_IP'], 5672))
channel = connection.channel()
channel.queue_declare(queue='lanit')


def callback(ch, method, properties, body):
	print(" [x] Received {}".format(body))


channel.basic_consume(queue='lanit', auto_ack=True, on_message_callback=callback)
print(' [*] Waiting... Press CTRL+C to exit.')
channel.start_consuming()
