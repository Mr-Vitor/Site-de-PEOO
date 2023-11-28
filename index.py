from tkinter import *
import pacientes, atendimentos






class Projeto():
    def __init__(self):
        #Criando a janela
        self.janela = Tk()
        self.janela.configure(bg='white')
        self.janela.geometry("{0}x{1}+0+0".format(self.janela.winfo_screenwidth(), self.janela.winfo_screenheight()))
        
        self.cabeçalho = Frame(self.janela, bg='#FEE040')
        self.cabeçalho.configure(width =self.cabeçalho.winfo_screenwidth(),height=70)
        self.cabeçalho.place(x=0,y=0)

        self.titulo = Label(self.janela,text='NomeProjeto',bg='#FEE040',font=("Georgia",25),fg='#960A0A')
        self.titulo.place(y=12,x=650)

        #Barra lateral
        self.barra_lateral = Frame(self.janela,bg='#F37B7B'
                                   )
        self.barra_lateral.configure(height=self.barra_lateral.winfo_screenheight(),width=400)
        self.barra_lateral.place(x=0,y=71)

        #botões
        self.nomes = ['Página Inicial','Pacientes','Atendimentos','Agenda','Sair']

        def configura_botão(num,comando):
            fonte = Button(self.janela,text=self.nomes[num],width=25,font=('Georgia',15),fg='#660606',relief='groove', bg='white',borderwidth=3,command=comando)
            
            
            return fonte


        self.pag_inicial = configura_botão(0,'')
        self.pag_inicial.place(x=25,y=130)
        self.pacientes = configura_botão(1,self.paci)
        self.pacientes.place(x=25,y=210)
        self.atendimentos = configura_botão(2,self.atend)
        self.atendimentos.place(x=25,y=290)
        self.agenda = configura_botão(3,'')
        self.agenda.place(x=25,y=380)
        self.sair = configura_botão(4,self.sair)
        self.sair.place(x=25,y=470)

        #imagem
        self.canvas = Canvas(self.janela,width=203,height=200,bg="#F37B7B",bd=0,highlightthickness=0)
        self.canvas.place(x=80,y=550)
        self.imagem = PhotoImage(file='clinica1.png').subsample(1)
        self.mostraImagem = self.canvas.create_image(100,100,image=self.imagem)

        #Tela principal

        Label(self.janela, text='AGENDA',fg='#960A0A',bg='white', font=('Itim',25)).place(x=900,y=110)

        #Exibindo agenda 

        #frame1 = Frame(self.janela, width=900,height=100,bg='#D9D9D9')
        #frame1.place(x=500,y=200)
        #frame2 = Frame(self.janela, width=900,height=100,bg='#D9D9D9')
        #frame2.place(x=500,y=350)
        #frame3 = Frame(#self.janela, width=900,height=100,bg='##D9D9D9')
        #frame3.place(x=500,y=500)
        #frame4 = Frame(#self.janela, width=900,height=100,bg='##D9D9D9')
        #frame4.place(x=500,y=650)

        

        yep = 200
        yep2 = [210,230,250,270]
        for c in range(4):
            Frame(self.janela, width=900,height=100,bg='#D9D9D9').place(x=500,y=yep)

            Label(self.janela,text='Data:  ',bg='#D9D9D9', font=('Itim',10)).place(x=515,y=yep2[0])
            Label(self.janela,text='Paciente :',bg='#D9D9D9', font=('Itim',10)).place(x=515,y=yep2[1])
            Label(self.janela,text='Médico : ',bg='#D9D9D9', font=('Itim',10)).place(x=515,y=yep2[2])
            Label(self.janela,text='Consulta : ',bg='#D9D9D9', font=('Itim',10)).place(x=515,y=yep2[3]) 
            
            for c in range(4):
                yep2[c]+=150
            yep+=150
        
        
        





        self.janela.mainloop()

    def paci(self):
        self.janela.destroy()
        pacientes.Pacientes()
    def atend(self):
        self.janela.destroy()
        atendimentos.Atendimentos()
    def sair(self):
        exit()
        
    

