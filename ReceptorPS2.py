import threading
import pika
from threading import Thread
 #credentials = pika.PlainCredentials('admin', 'ads2020')

 #connection = pika.BlockingConnection(
 #    pika.ConnectionParameters('localhost',
 #                                    5672,
 #                                    '/',
 #                                    credentials))

class ReceptorPS2(threading.Thread):
    def __init__(self, usuario, messenger):
        Thread.__init__(self)
        self.messenger = messenger
        self.usuario = usuario

    def run(self):
        def callback(ch, method, properties, body):
            print(" [x] %r" % body)
            messenger = self.messenger
            messenger.receberMsg(body)

        params = pika.URLParameters('amqps://grlcqibb:dkC9dlyz6p9v55ErECes8KXmSvDiiDd7@jackal.rmq.cloudamqp.com/grlcqibb')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.exchange_declare(exchange='Pythonistas', exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='Pythonistas', queue=queue_name)
        print(' [*] Aguardando mensagem em Pythonistas.')
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
            