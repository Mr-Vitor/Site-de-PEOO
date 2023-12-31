from tkinter import *
import atendimentos, login, pacientes, sqlite3

class Projeto():
    def __init__(self):
        #Criando a janela
        self.janela = Tk()
        self.janela.configure(bg='white')
        self.janela.geometry("{0}x{1}+0+0".format(self.janela.winfo_screenwidth(), self.janela.winfo_screenheight()))
        
        self.cabeçalho = Frame(self.janela, bg='#87e9c9')
        self.cabeçalho.configure(width =self.cabeçalho.winfo_screenwidth(),height=70)
        self.cabeçalho.place(x=0,y=0)

        self.titulo = Label(self.janela,text='Clinic +',bg='#87e9c9',font=("Georgia",25),fg='white')
        self.titulo.place(y=12,x=650)

        #Barra lateral
        self.barra_lateral = Frame(self.janela,bg='#87e9c9'
                                   )
        self.barra_lateral.configure(height=self.barra_lateral.winfo_screenheight(),width=400)
        self.barra_lateral.place(x=0,y=71)

        #botões
        self.nomes = ['Página Inicial','Pacientes','Atendimentos','Login','Sair']

        def configura_botão(num,comando):
            fonte = Button(self.janela,text=self.nomes[num],width=25,font=('Georgia',15),fg='#38a680',
                            relief='groove', bg='white',borderwidth=3,command=comando)
            
            return fonte

        #Botões laterais
        self.pag_inicial = configura_botão(0,'')
        self.pag_inicial.place(x=25,y=130)
        self.pacientes = configura_botão(1,self.paci)
        self.pacientes.place(x=25,y=210)
        self.atendimentos = configura_botão(2,self.atend)
        self.atendimentos.place(x=25,y=290)
        self.login = configura_botão(3,self.logi)
        self.login.place(x=25,y=380)
        self.quit = configura_botão(4,self.sair)
        self.quit.place(x=25,y=470)

        #imagem
        self.canvas = Canvas(self.janela,width=203,height=200,bg="#87e9c9",bd=0,highlightthickness=0)
        self.canvas.place(x=80,y=550)
        self.imagem = PhotoImage(file='clinica1.png').subsample(3)
        self.mostraImagem = self.canvas.create_image(100,100,image=self.imagem)

        #Tela principal

        Label(self.janela, text='AGENDA',fg='#38a680',bg='white', font=('Itim',25)).place(x=900,y=110)

        #Exibindo agenda 
        yep = 200
        yep2 = [210,230,250,270]
        for c in range(4):
            #Dicionário para armazenar os dados do BD
            self.agenda = {'Paciente' : '',
                           'Médico' : '',
                           'Consulta' : '',
                           'Data' : ''}

            Frame(self.janela, width=900,height=100,bg='#87e9c9').place(x=500,y=yep)

            #Cria os Frames com as informações do dicionário
            self.nome_paci = Label(self.janela, text='Paciente: ', bg='#87e9c9', font=('Itim',10))
            self.nome_paci.place(x=515,y=yep2[0])

            self.nome_doc = Label(self.janela, text='Médico: ', bg='#87e9c9', font=('Itim',10))
            self.nome_doc.place(x=515,y=yep2[1])

            self.cons = Label(self.janela, text='Consulta: ', bg='#87e9c9', font=('Itim',10))
            self.cons.place(x=515,y=yep2[2]) 

            self.data = Label(self.janela, text='Data:  ', bg='#87e9c9', font=('Itim',10))
            self.data.place(x=515,y=yep2[3])

            #Insere os valores do DB no dicionário
            con = sqlite3.connect('Banco_principal.db')
            sql = con.cursor()
            self.cadastro = sql.execute("SELECT * FROM ATENDIMENTOS WHERE id = ?" , (str(c+1)))
            self.resultado = self.cadastro.fetchone()

            if(self.resultado):
                #Caso o id retorne um valor, atualiza a agenda
                self.agenda['Paciente'] = self.resultado[1]
                self.agenda['Médico'] = self.resultado[3]
                self.agenda['Consulta'] = self.resultado[5]
                self.agenda['Data'] = self.resultado[4]

                self.nome_paci.configure(text = f"Paciente: {self.agenda['Paciente']}")
                self.nome_doc.configure(text= f"Médico: {self.agenda['Médico']}")
                self.cons.configure(text= f"Consulta: {self.agenda['Consulta']}")
                self.data.configure(text= f"Data: {self.agenda['Data']}")
            else:
                #Caso não retorne, Deixa vazio
                self.nome_paci.configure(text = "Paciente: N/A")
                self.nome_doc.configure(text= f"Médico: N/A")
                self.cons.configure(text= f"Consulta: N/A")
                self.data.configure(text= f"Data: N/A")

            con.close()

            for c in range(4):
                #Atualiza a posição do próximo frame da agenda
                yep2[c]+=150
            yep+=150
        
        self.janela.mainloop()

    def paci(self):
        #Abre a janela pacientes
        self.janela.destroy()
        pacientes.Pacientes()

    def atend(self):
        #Abre a janela Atendimentos
        self.janela.destroy()
        atendimentos.Atendimentos()

    def logi(self):
        #Abre a janela Login
        self.janela.destroy()
        login.Login()

    def sair(self):
        #Fecha o App
        exit()