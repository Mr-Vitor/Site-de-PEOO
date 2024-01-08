from tkinter import *
import index

class Login:
    def __init__(self):
        #Criando a janela
        self.janela = Tk()
        self.janela.geometry("{0}x{1}+0+0".format(self.janela.winfo_screenwidth(), self.janela.winfo_screenheight()))

        self.cabeçalho = Frame(self.janela, bg='#87e9c9')
        self.cabeçalho.configure(width =self.cabeçalho.winfo_screenwidth(),height=70)
        self.cabeçalho.place(x=0,y=0)

        self.titulo = Label(self.janela,text='Clinic +',bg='#87e9c9',font=("Georgia",25),fg='white')
        self.titulo.place(y=12,x=650)
        
        #importanto estrutura base
        
        #titulo da seção
        self.titulo = Label(self.janela,text='LOGIN',fg="#38a680",font=('Comic',20))
        self.titulo.place(y=110,x=680)

        #criando formulário
        self.quadro = Frame(self.janela,width=1200,height=350,bg="#D9D9D9")
        self.quadro.place(x=200,y=320)
        letra = ('Arial',22)

        #primeira linha
        Label(self.janela,text='USUÁRIO: ',bg='#D9D9D9',fg="blue", font=('Arial',12)).place(x=240,y=360)

        self.usuario = Entry(self.janela,width=60,font=letra)
        self.usuario.place(x=240,y=390)

        #segunda linha
        Label(self.janela,text='SENHA:  ',bg='#D9D9D9',fg="blue", font=('Arial',12)).place(x=240,y=440)

        self.senha = Entry(self.janela,width=60,font=letra)
        self.senha.place(x=240,y=480)

        self.login = Button(self.janela,width=40,height=2,fg="white",text='ENTRAR',font=('Comic',12),command=self.entrar,bg='blue')
        self.login.place(x=540,y=570) 

        self.janela.mainloop()
   
    def entrar(self):
         #Abre a página inicial
         self.janela.destroy()
         index.Projeto()