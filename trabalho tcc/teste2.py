from tkinter import *
import teste, teste3

class Projeto():
    def __init__(self):
        #Criando a janela
        self.janela = Tk()
        self.janela.geometry("{0}x{1}+0+0".format(self.janela.winfo_screenwidth(), self.janela.winfo_screenheight()))
        
        self.cabeçalho = Frame(self.janela, bg='#FEE040')
        self.cabeçalho.configure(width =self.cabeçalho.winfo_screenwidth(),height=70)
        self.cabeçalho.place(x=0,y=0)

        self.titulo = Label(self.janela,text='NomeProjeto',bg='#FEE040',font=("Georgia",25),fg='#960A0A')
        self.titulo.place(y=12,x=650)

        #Barra lateral
        self.barra_lateral = Frame(self.janela,bg='#660606')
        self.barra_lateral.configure(height=self.barra_lateral.winfo_screenheight(),width=400)
        self.barra_lateral.place(x=0,y=71)

        #botoões
        #fonte = ('Georgia',15)
        self.nomes = ['Página Inicial','Pacientes','Atendimentos','Agenda','Sair']

        def configura_botão(num,comando):
            fonte = Button(self.janela,text=self.nomes[num],width=25,font=('Georgia',15),fg='#660606',relief='groove',command=comando)
            
            
            return fonte


        self.pag_inicial = configura_botão(0,'')
        self.pag_inicial.place(x=25,y=130)
        self.pacientes = configura_botão(1,self.paci)
        self.pacientes.place(x=25,y=210)
        self.atendimentos = configura_botão(2,self.atend)
        self.atendimentos.place(x=25,y=290)
        self.agenda = configura_botão(3,'')
        self.agenda.place(x=25,y=380)
        self.sair = configura_botão(4,self.saida)
        self.sair.place(x=25,y=470)



        self.janela.mainloop()

    def paci(self):
        self.janela.destroy()
        teste.Pacientes()
    def atend(self):
        self.janela.destroy()
        teste3.Atendimentos()
    

    
    def saida(self):
        exit()