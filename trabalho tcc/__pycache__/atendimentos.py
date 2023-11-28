from tkinter import *
import teste2


class Atendimentos():
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

        #titulo da seção
        self.titulo = Label(self.janela,text='ATENDIMENTOS',fg=cor_letra,font=('Comic',20))
        self.titulo.place(y=110,x=650)

        #Criando botões
        self.borda1 = Frame(self.janela,bg=cor_letra,width=329,height=72)
        self.borda1.place(x=200,y=180) 

        self.cria_atendimento = Button(self.janela,width=35,height=3,fg=cor_letra,text='Criar Atendimento',font=('Comic',12))
        self.cria_atendimento.place(x=202,y=182) 

        self.borda2 = Frame(self.janela,bg=cor_letra,width=329,height=72)
        self.borda2.place(x=600,y=180) 

        self.editar_atendimento = Button(self.janela,width=35,height=3,fg=cor_letra,text='Editar Atendimento',font=('Comic',12))
        self.editar_atendimento.place(x=602,y=182) 

        self.borda3 = Frame(self.janela,bg=cor_letra,width=329,height=72)
        self.borda3.place(x=1000,y=180) 
        
        self.excluir_atendimento = Button(self.janela,width=35,height=3,fg=cor_letra,text='Excluir Atendimento',font=('Comic',12))
        self.excluir_atendimento.place(x=1002,y=182) 


        #criando formulário
        self.quadro = Frame(self.janela,width=1400,height=350,bg="#D9D9D9")
        self.quadro.place(x=60,y=300)
        letra = ('Arial',22)

        #primeira linha
        Label(self.janela,text='Nome: ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=100,y=340)

        self.nome = Entry(self.janela,width=45,font=letra)
        self.nome.place(x=100,y=370)

        Label(self.janela,text='CPF: ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=900,y=340)

        self.cpf = Entry(self.janela,width=27,font=letra)
        self.cpf.place(x=900,y=370)

        #segunda linha
        Label(self.janela,text='Médico(a): ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=100,y=420)

        self.nome_medico = Entry(self.janela,width=45,font=letra)
        self.nome_medico.place(x=100,y=460)
        
        Label(self.janela,text='Data:  ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=900,y=420)

        self.data = Entry(self.janela,width=27,font=letra)
        self.data.place(x=900,y=460)

        #terceira linha
        Label(self.janela,text='Tipo da consulta: ',bg='#D9D9D9',fg=cor_letra, font=('Arial',12)).place(x=100,y=510)

        self.consulta = Entry(self.janela,width=45,font=letra)
        self.consulta.place(x=100,y=550)

        self.borda4 = Frame(self.janela, width=254, height=48, bg=cor_letra)
        self.borda4.place(x=1000, y=550)

        self.btn_confirmar = Button(self.janela, width=30, height=2, fg=cor_letra,text='Cadastrar',font=('Comic',10))
        self.btn_confirmar.place(x=1002,y=552)

        self.volta = Button(self.janela,text='<- Página inicial ',command=self.voltar)
        self.volta.place(x=40,y=750)
    
    def voltar(self):
        self.janela.destroy()
        teste2.Projeto()