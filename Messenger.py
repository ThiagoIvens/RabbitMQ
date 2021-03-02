#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 24, 2021 07:53:34 AM -03  platform: Windows NT

import pika
import tkinter as tk
import ReceptorFila
import ReceptorPS

class Messenger(tk.Tk):
    def __init__(self, user):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _ana1color = '#a3a3a3'
        _ana2color = '#ececec'

        tk.Tk.__init__(self)

        self.geometry("600x450+468+138")
        self.minsize(120, 1)
        self.maxsize(1540, 845)
        self.resizable(1,  1)
        self.title("Messenger da Deep Web")
        self.configure(background=_bgcolor)
        
        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.017, rely=0.022, relheight=0.967, relwidth=0.975)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background=_bgcolor)

        self.Labelframe1 = tk.LabelFrame(self.Frame1)
        self.Labelframe1.place(relx=0.017, rely=0.023, relheight=0.747, relwidth=0.239)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground=_fgcolor)
        self.Labelframe1.configure(text='''Usuarios''')
        self.Labelframe1.configure(background=_bgcolor)

        self.ListUsers = tk.Listbox(self.Labelframe1)
        self.ListUsers.place(relx=0.070, rely=0.060, relheight=0.600, relwidth=0.880, bordermode='ignore')
        self.ListUsers.configure(background="white")
        self.ListUsers.configure(disabledforeground=_ana1color)
        self.ListUsers.configure(font="TkFixedFont")
        self.ListUsers.configure(foreground=_fgcolor)
        def userEvent(event):
            index = self.ListUsers.curselection()
            self.receptor =  self.ListUsers.get(index)
        self.ListUsers.bind('<ButtonRelease-1>', userEvent)
        
        self.Label = tk.Label(self.Labelframe1)
        self.Label.place(relx=0.070, rely=0.665, relheight=0.050, relwidth=0.700)
        self.Label.configure(relief='groove')
        self.Label.configure(foreground=_fgcolor)
        self.Label.configure(text='''Grupos''')
        self.Label.configure(background=_bgcolor)

        self.ListGroup = tk.Listbox(self.Labelframe1)
        self.ListGroup.place(relx=0.070, rely=0.720, relheight=0.200, relwidth=0.880, bordermode='ignore')
        self.ListGroup.configure(background="white")
        self.ListGroup.configure(disabledforeground=_ana1color)
        self.ListGroup.configure(font="TkFixedFont")
        self.ListGroup.configure(foreground=_fgcolor)
        def groupEvent(event):
            index = self.Users.curselection()
            self.receptor =  self.ListGroup.get(index)
        self.ListGroup.bind('<ButtonRelease-1>', groupEvent)

        self.Labelframe2 = tk.LabelFrame(self.Frame1)
        self.Labelframe2.place(relx=0.274, rely=0.023, relheight=0.800, relwidth=0.700)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground=_fgcolor)
        self.Labelframe2.configure(text='''Mensagens''')
        self.Labelframe2.configure(background=_bgcolor)

        self.msgs = tk.Message(self.Labelframe2)
        self.msgs.place(relx=0.048, rely=0.062, relheight=0.700, relwidth=0.600, bordermode='ignore')
        self.msgs.configure(anchor='nw')
        self.msgs.configure(background=_bgcolor)
        self.msgs.configure(foreground=_fgcolor)
        self.msgs.configure(highlightbackground=_bgcolor)
        self.msgs.configure(highlightcolor=_fgcolor)
        self.msgs.configure(width=190)
        
        self.inputMsg = tk.Entry(self.Frame1)
        self.inputMsg.place(relx=0.017, rely=0.828, height=40, relwidth=0.793)
        self.inputMsg.configure(background="white")
        self.inputMsg.configure(cursor="fleur")
        self.inputMsg.configure(disabledforeground=_ana1color)
        self.inputMsg.configure(font="TkFixedFont")
        self.inputMsg.configure(foreground=_fgcolor)
        self.inputMsg.configure(insertbackground=_fgcolor)

        self.btnEnviar = tk.Button(self.Frame1)
        self.btnEnviar.place(relx=0.838, rely=0.828, height=44, width=67)
        self.btnEnviar.configure(activebackground=_ana2color)
        self.btnEnviar.configure(activeforeground=_fgcolor)
        self.btnEnviar.configure(background=_bgcolor)
        self.btnEnviar.configure(disabledforeground=_ana1color)
        self.btnEnviar.configure(foreground=_fgcolor)
        self.btnEnviar.configure(highlightbackground=_bgcolor)
        self.btnEnviar.configure(highlightcolor=_fgcolor)
        self.btnEnviar.configure(pady="0")
        self.btnEnviar.configure(text='''Enviar''')
        self.btnEnviar.configure(command=lambda:self.enviarMsg)

        #Inicia as Threads
        td = ReceptorFila.ReceptorFila(self)
        tr = ReceptorPS.ReceptorPS(self)
        #td.start()
        #tr.start()
    
    def enviarMsg(self):
        msg = ": " + self.inputMsg.get()
        print('enviando: '+ msg)
        self.msgs["text"] += msg +'\n'

        params = pika.URLParameters('amqps://grlcqibb:dkC9dlyz6p9v55ErECes8KXmSvDiiDd7@jackal.rmq.cloudamqp.com/grlcqibb')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        usuario = "thiago"
        if(self.receptor == "Público"):
            # EmissorPS
            channel.exchange_declare(exchange=self.receptor, exchange_type='fanout')
            mensagem = usuario + " (Público)" + msg
            channel.basic_publish(exchange=self.receptor, routing_key='', body=mensagem)
            print(" [x] Enviado para o Grupo %r" % mensagem)
            connection.close()
        else:
            #EmissorFila
            channel.queue_declare(queue=self.receptor, durable=True)
            mensagem = usuario + msg
            mensagem = mensagem.encode('utf-8')
            channel.basic_publish(exchange='', routing_key='thiago', body=mensagem)
            connection.close()
        self.inputMsg.delete(0, tk.END)   
        return 
            
        
    def receberMsg(self, body):
        self.msgs["text"] += body.decode('utf-8') + "\n"