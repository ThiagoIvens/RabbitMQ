import threading
import pika
from threading import Thread

class ReceptorFila(threading.Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent
    
    def callback(self, ch, method, properties, body):
        print(" [x] Mensagem recebida %r" % body.decode('utf-8'))
        r = self.parent
        r.receberMsg(body)

    def run(self):
        params = pika.URLParameters('amqps://grlcqibb:dkC9dlyz6p9v55ErECes8KXmSvDiiDd7@jackal.rmq.cloudamqp.com/grlcqibb')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.basic_consume(queue='thiago', on_message_callback=self.callback, auto_ack=True)
        print(' [*] Aguardando mensagens')
        channel.start_consuming()
        