from tkinter import *
import index, sqlite3

con = sqlite3.connect('Banco_principal.db')
sql = con.cursor()

listaTabelas = sql.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ATENDIMENTOS'")

if listaTabelas.fetchone()[0]!=1 :
    sql.execute("CREATE TABLE ATENDIMENTOS (nome, cpf, medico, data, consulta)")

con.close()

class Atendimentos():
    def __init__(self) -> None:
        #Criando a janela
        self.janela = Tk()
        self.janela.configure(bg='white')
        self.janela.geometry("{0}x{1}+0+0".format(self.janela.winfo_screenwidth(), self.janela.winfo_screenheight()))
        self.cor_letra = 'blue'

        self.cabeçalho = Frame(self.janela, bg='#87e9c9')
        self.cabeçalho.configure(width =self.cabeçalho.winfo_screenwidth(),height=70)
        self.cabeçalho.place(x=0,y=0)

        self.titulo = Label(self.janela,text='NomeProjeto',bg='#87e9c9',font=("Georgia",25),fg='white')
        self.titulo.place(y=12,x=650)

        #titulo da seção
        self.titulo = Label(self.janela, text='ATENDIMENTOS',fg='#38a680',bg='white', font=('Itim',25))
        self.titulo.place(y=110,x=680)

        #Criando botões
        self.borda1 = Frame(self.janela,bg='blue',width=329,height=72)
        self.borda1.place(x=200,y=180) 

        self.cria_atendimento = Button(self.janela,bg='white', width=35,height=3,fg='blue',text='Criar Atendimento',font=('Comic',12), command=self.adiconaAtend)
        self.cria_atendimento.place(x=202,y=182) 

        self.borda2 = Frame(self.janela,bg='blue',width=329,height=72)
        self.borda2.place(x=600,y=180) 

        self.editar_atendimento = Button(self.janela,bg='white', width=35,height=3,fg='blue',text='Editar Atendimento',font=('Comic',12), command=self.editarAtend)
        self.editar_atendimento.place(x=602,y=182) 

        self.borda3 = Frame(self.janela,bg='blue',width=329,height=72)
        self.borda3.place(x=1000,y=180) 
        
        self.excluir_atendimento = Button(self.janela,bg='white', width=35,height=3,fg='blue',text='Excluir Atendimento',font=('Comic',12), command=self.deleteAtend)
        self.excluir_atendimento.place(x=1002,y=182) 


        #criando formulário
        self.quadro = Frame(self.janela,width=1400,height=350,bg="#D9D9D9")
        self.quadro.place(x=60,y=300)
        letra = ('Arial',20)
        self.error_span = []

        #primeira linha
        Label(self.janela,text='Nome: ',bg='#D9D9D9',fg='blue', font=('Arial',12)).place(x=100,y=320)

        self.nome = Entry(self.janela,width=45,font=letra)
        self.nome.place(x=100,y=350)

        self.nome_span = Label(self.janela, text='Nome inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.nome_span.place(x=100, y=390)
        self.error_span.append(self.nome_span)

        Label(self.janela,text='CPF: ',bg='#D9D9D9',fg='blue', font=('Arial',12)).place(x=900,y=320)

        self.cpf = Entry(self.janela,width=27,font=letra)
        self.cpf.place(x=900,y=350)

        self.cpf_span = Label(self.janela, text='CPF inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.cpf_span.place(x=900, y=390)

        #segunda linha
        Label(self.janela,text='Médico(a): ',bg='#D9D9D9',fg='blue', font=('Arial',12)).place(x=100,y=430)

        self.nome_medico = Entry(self.janela,width=45,font=letra)
        self.nome_medico.place(x=100,y=460)

        self.nome_medico_span = Label(self.janela, text='Nome inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.nome_medico_span.place(x=100, y=500)
        self.error_span.append(self.nome_medico_span)
        
        Label(self.janela,text='Data:  ',bg='#D9D9D9',fg='blue', font=('Arial',12)).place(x=900,y=430)

        self.data = Entry(self.janela,width=27,font=letra)
        self.data.place(x=900,y=460)

        self.data_span = Label(self.janela, text='Data inválida', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.data_span.place(x = 900, y=500)
        self.error_span.append(self.data_span)

        #terceira linha
        Label(self.janela,text='Tipo da consulta: ',bg='#D9D9D9',fg='blue', font=('Arial',12)).place(x=100,y=540)

        self.consulta = Entry(self.janela,width=45,font=letra)
        self.consulta.place(x=100,y=570)

        self.consulta_span = Label(self.janela, text='Nome inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.consulta_span.place(x=100, y=610)
        self.error_span.append(self.consulta_span)

        self.borda4 = Frame(self.janela, width=254, height=48, bg=self.cor_letra)

        self.btn_confirmar = Button(self.janela, width=30, height=2,bg='blue', fg='white',text='Cadastrar',font=('Comic',10), command=self.attAtend)

        self.volta = Button(self.janela,text='<- Página inicial ',height=2,command=self.voltar,fg='blue',bg="#87e9c9")
        self.volta.place(x=40,y=700)
        self.janela.mainloop()
    
    def voltar(self):
        self.janela.destroy()
        index.Projeto()

    def adiconaAtend(self):
        self.ok = 0
        self.lista_entry = []
        self.entry_nome = self.nome.get()
        self.lista_entry.append(self.entry_nome)

        self.entry_cpf = self.cpf.get()

        self.entry_doc = self.nome_medico.get()
        self.lista_entry.append(self.entry_doc)

        self.entry_data = self.data.get()
        self.lista_entry.append(self.entry_data)

        self.entry_consulta = self.consulta.get()
        self.lista_entry.append(self.entry_consulta)

        for i in range(len(self.lista_entry)):
            try:
                if(self.lista_entry[i] == ''):
                    print(1/0)
            except:
                self.error_span[i].configure(fg = self.cor_letra)
            else:
                self.error_span[i].configure(fg = '#D9D9D9')
                self.ok += 1
        
        if(self.entry_cpf.isnumeric() == False):
            self.cpf_span.configure(fg = self.cor_letra)
        else:
            self.cpf_span.configure(fg = '#D9D9D9')
            self.ok += 1

        if(self.ok == 5):
            con = sqlite3.connect('Banco_principal.db')
            sql = con.cursor()
            sql.execute("""INSERT INTO ATENDIMENTOS (nome, cpf, medico, data, consulta)
                        VALUES (?,?,?,?,?)""", (self.entry_nome, self.entry_cpf, self.entry_doc,
                        self.entry_data, self.entry_consulta))
            con.commit()
            con.close()

            self.nome.delete(0, END)
            self.cpf.delete(0, END)
            self.nome_medico.delete(0, END)
            self.data.delete(0, END)
            self.consulta.delete(0, END)

            self.cpf_span.configure(fg = '#D9D9D9')
            for i in range(len(self.lista_entry)):
                self.error_span[i].configure(fg = '#D9D9D9')
            self.nome_span.configure(text='Cadastro realizado', fg = self.cor_letra)


    def editarAtend(self):

        self.att_nome = self.nome.get()

        if(self.att_nome == '' or self.cpf.get() == ''):
            self.nome_span.configure(fg = self.cor_letra, text='Digite um nome e cpf para editar')
        else:
            self.borda4.place(x=1000, y=550)
            self.btn_confirmar.place(x=1002,y=552)

            con = sqlite3.connect('Banco_principal.db')
            sql = con.cursor()

            self.cadastro = sql.execute(f"SELECT count(nome) FROM ATENDIMENTOS WHERE nome = ? AND cpf = ?", (self.att_nome, self.cpf.get()))
            self.resultado = self.cadastro.fetchone()

            if self.resultado[0] < 1:
                self.nome_span.configure(fg = self.cor_letra, text= 'Atendimento não cadastrado')
                con.close()

            else:
                self.nome_span.configure(fg = '#D9D9D9', text='')
                self.cadastro = sql.execute("SELECT * FROM ATENDIMENTOS WHERE nome = ? ", (self.att_nome))
                self.resultado = self.cadastro.fetchone()

                self.cpf.delete(0, END)
                self.nome_medico.delete(0, END)
                self.data.delete(0, END)
                self.consulta.delete(0, END)

                self.cpf.insert(0, self.resultado[1])
                self.nome_medico.insert(0, self.resultado[2])
                self.data.insert(0, self.resultado[3])
                self.consulta.insert(0, self.resultado[4])
                con.close()
    
    def attAtend(self):
        con = sqlite3.connect('Banco_principal.db')
        sql = con.cursor()

        sql.execute("UPDATE ATENDIMENTOS SET nome = ?, cpf = ?, medico = ?, data = ?, consulta = ? WHERE nome = ?",
                    (self.nome.get(), self.cpf.get(), self.nome_medico.get(), self.data.get(), self.consulta.get(), self.att_nome)) 

        con.commit()
        con.close()
    
    def deleteAtend(self):

        if(self.cpf.get() == ''):
            self.cpf_span.configure(fg = self.cor_letra, text='Digite um CPF cadastrado para excluir')
        else:
            con = sqlite3.connect('Banco_principal.db')
            sql = con.cursor()

            self.cadastro = sql.execute(f"SELECT count(cpf) FROM ATENDIMENTOS WHERE nome = ? AND cpf = ? ", (self.nome.get(), self.cpf.get()))
            self.resultado = self.cadastro.fetchone()

            if self.resultado[0] < 1:
                self.cpf_span.configure(fg = self.cor_letra, text= 'Nome/CPF não cadastrado')
                con.close()

            else:
                sql.execute("DELETE FROM ATENDIMENTOS WHERE cpf = ?", (self.cpf.get())) 

                self.nome.delete(0, END)
                self.cpf.delete(0, END)
                self.nome_medico.delete(0, END)
                self.data.delete(0, END)
                self.consulta.delete(0, END)

                self.nome_span.configure(fg= self.cor_letra, text='Atendimento excluído')

                con.commit()
                con.close()