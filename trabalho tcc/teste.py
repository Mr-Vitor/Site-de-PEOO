from tkinter import *
import teste2


class Pacientes:
    def __init__(self) -> None:
        #Criando a janela
        self.janela = Tk()
        self.janela.geometry("{0}x{1}+0+0".format(self.janela.winfo_screenwidth(), self.janela.winfo_screenheight()))
        cor_letra = '#660606'

        
        self.cabeçalho = Frame(self.janela, bg='#FEE040')
        self.cabeçalho.configure(width =self.cabeçalho.winfo_screenwidth(),height=70)
        self.cabeçalho.place(x=0,y=0)

        self.titulo = Label(self.janela,text='NomeProjeto',bg='#FEE040',font=("Georgia",25),fg='#960A0A')
        self.titulo.place(y=12,x=650)
        
        #importanto estrutura base
        
        #titulo da seção
        self.titulo = Label(self.janela,text='PACIENTES',fg=cor_letra,font=('Comic',20))
        self.titulo.place(y=110,x=650)

        #criando botões
        self.borda1 = Frame(self.janela,bg=cor_letra,width=375,height=72)
        self.borda1.place(x=100,y=180) 

        self.adicona_paciente = Button(self.janela,width=40,height=3,fg=cor_letra,text='Adicionar Paciente',font=('Comic',12))
        self.adicona_paciente.place(x=102,y=182) 

        self.borda2 = Frame(self.janela,bg=cor_letra,width=375,height=72)
        self.borda2.place(x=1000,y=180) 
        self.editar_paciente = Button(self.janela,width=40,height=3,fg=cor_letra,text='Editar Paciente',font=('Comic',12))
        self.editar_paciente.place(x=1002,y=182) 

        #criando formulário
        self.quadro = Frame(self.janela,width=1400,height=350,bg="#D9D9D9")
        self.quadro.place(x=60,y=320)
        letra = ('Arial',22)

        #primeira linha
        Label(self.janela,text='Nome: ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=100,y=360)

        self.nome = Entry(self.janela,width=60,font=letra)
        self.nome.place(x=100,y=390)

        #segunda linha
        Label(self.janela,text='CPF: ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=100,y=440)

        self.cpf = Entry(self.janela,width=20,font=letra)
        self.cpf.place(x=100,y=480)

        Label(self.janela,text='N° do SUS:  ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=600,y=440)

        self.sus = Entry(self.janela,width=20,font=letra)
        self.sus.place(x=600,y=480)
        
        Label(self.janela,text='Idade:  ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=1100,y=440)

        self.idade = Entry(self.janela,width=10,font=letra)
        self.idade.place(x=1100,y=480)

        #terceira linha
        Label(self.janela,text='Telefone: ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=100,y=530)

        self.telefone = Entry(self.janela,width=20,font=letra)
        self.telefone.place(x=100,y=570)

        Label(self.janela,text='CEP:  ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=600,y=530)

        self.cep = Entry(self.janela,width=20,font=letra)
        self.cep.place(x=600,y=570)
        
        Label(self.janela,text='Estado:  ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=1100,y=530)

        self.estado = Entry(self.janela,width=10,font=letra)
        self.estado.place(x=1100,y=570)

        self.volta = Button(self.janela,text='<- Página inicial ',command=self.voltar)
        self.volta.place(x=40,y=750)
    
    def voltar(self):
        self.janela.destroy()
        teste2.Projeto()

        



        

