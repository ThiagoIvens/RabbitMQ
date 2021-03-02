import tkinter as tk
from User import User

class Cadastro(tk.Tk):
    def __init__(self):
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        tk.Tk.__init__(self)

        self.geometry("600x450+468+138")
        self.minsize(120, 1)
        self.maxsize(1540, 845)
        self.resizable(1,  1)
        self.title("Cadastrar")
        self.configure(background="#000000")

        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.25, rely=0.178, relheight=0.567, relwidth=0.525)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#008000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.032, rely=0.039, height=41, width=294)
        self.Label1.configure(activebackground="#000000")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#008000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Wide Latin} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Cadastrar''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.127, rely=0.235, height=21, width=244)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#008000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(justify='left')
        self.Label2.configure(text='''Usuario:''')

        self.cadastraruser = tk.Entry(self.Frame1)
        self.cadastraruser.place(relx=0.127, rely=0.314, height=20, relwidth=0.775)
        self.cadastraruser.configure(background="white")
        self.cadastraruser.configure(disabledforeground="#a3a3a3")
        self.cadastraruser.configure(font="TkFixedFont")
        self.cadastraruser.configure(foreground="#000000")
        self.cadastraruser.configure(insertbackground="black")

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.127, rely=0.471, height=21, width=244)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#008000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Senha:''')

        self.cadastrarpassword = tk.Entry(self.Frame1)
        self.cadastrarpassword.place(relx=0.127, rely=0.549, height=20, relwidth=0.775)
        self.cadastrarpassword.configure(background="white")
        self.cadastrarpassword.configure(disabledforeground="#a3a3a3")
        self.cadastrarpassword.configure(font="TkFixedFont")
        self.cadastrarpassword.configure(foreground="#000000")
        self.cadastrarpassword.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame1, command=self.registrar)
        self.Button1.place(relx=0.317, rely=0.745, height=24, width=117)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#c0c0c0")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#ffffff")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Cadastrar''')

    def registrar(self):
        user = User()
        users = user.selectAllUsers()
        user.usuario = self.cadastraruser.get()
        user.senha = self.cadastrarpassword.get()

        for usuarios in users:
            if usuarios[1] == user.usuario:
                if usuarios[2] == user.senha:
                    self.Label1["text"] = "Usuário já cadastrado."
                    break
                else:
                    continue
            else:
                continue
        else:
            if "".__eq__(user.usuario):
                if "".__eq__(user.senha):
                   self.Label1["text"] = "Um ou mais campos estão vazios."
                   return
            self.Label1["text"] = user.insertUser()
            self.cadastraruser.delete(0, tk.END)
            self.cadastrarpassword.delete(0, tk.END)
            self.destroy()