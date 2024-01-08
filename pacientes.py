from tkinter import *
import index, sqlite3
from math import trunc

class Pacientes:
    def __init__(self) -> None:
        con = sqlite3.connect('Banco_principal.db')
        sql = con.cursor()
        listaTabelas = sql.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='PACIENTES'")

        if listaTabelas.fetchone()[0]!=1 :
            sql.execute("CREATE TABLE PACIENTES (nome, cpf, sus, idade, telefone, cep, uf)")
            con.commit()

        con.close()

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
        
        #importando estrutura base
        
        #titulo da seção
        self.titulo = Label(self.janela,text='PACIENTES',fg=self.cor_letra, bg='white',font=('Comic',20))
        self.titulo.place(y=110,x=680)

        #criando botões
        self.borda1 = Frame(self.janela,bg=self.cor_letra,width=375,height=72)
        self.borda1.place(x=100,y=180) 

        self.adicona_paciente = Button(self.janela,width=40,height=3,fg=self.cor_letra,text='Adicionar Paciente',font=('Comic',12), command= self.adiconaPaciente)
        self.adicona_paciente.place(x=102,y=182) 

        self.borda2 = Frame(self.janela,bg=self.cor_letra,width=375,height=72)
        self.borda2.place(x=1000,y=180) 
        self.editar_paciente = Button(self.janela,width=40,height=3,fg=self.cor_letra,text='Editar Paciente',font=('Comic',12), command= self.editarPaciente)
        self.editar_paciente.place(x=1002,y=182) 

        #criando formulário
        self.quadro = Frame(self.janela,width=1400,height=350,bg="#D9D9D9")
        self.quadro.place(x=60,y=320)
        letra = ('Arial',20)
        self.error_span = []

        #primeira linha
        Label(self.janela,text='Nome: ',bg='#D9D9D9',fg=self.cor_letra, font=('Arial',12)).place(x=100,y=340)

        self.nome = Entry(self.janela,width=60,font=letra)
        self.nome.place(x=100,y=370)

        self.nome_span = Label(self.janela, text='Nome inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.nome_span.place(x=100,y=410)

        #segunda linha
        Label(self.janela,text='CPF: ',bg='#D9D9D9',fg=self.cor_letra, font=('Arial',12)).place(x=100,y=450)

        self.cpf = Entry(self.janela,width=20,font=letra)
        self.cpf.place(x=100,y=480)

        self.cpf_span = Label(self.janela, text='CPF inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.cpf_span.place(x=100,y=520)
        self.error_span.append(self.cpf_span)

        Label(self.janela,text='N° do SUS:  ',bg='#D9D9D9', fg=self.cor_letra, font=('Arial',12)).place(x=600,y=450)

        self.sus = Entry(self.janela,width=20,font=letra)
        self.sus.place(x=600,y=480)

        self.sus_span = Label(self.janela, text='Nº do SUS inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.sus_span.place(x=600,y=520)
        self.error_span.append(self.sus_span)
        
        Label(self.janela,text='Idade:  ',bg='#D9D9D9',fg=self.cor_letra, font=('Arial',12)).place(x=1100,y=450)

        self.idade = Entry(self.janela,width=10,font=letra)
        self.idade.place(x=1100,y=480)

        self.idade_span = Label(self.janela, text='Idade inválida', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.idade_span.place(x=1100,y=520)
        self.error_span.append(self.idade_span)

        #terceira linha
        Label(self.janela,text='Telefone: ',bg='#D9D9D9',fg=self.cor_letra, font=('Arial',12)).place(x=100,y=560)

        self.telefone = Entry(self.janela,width=20,font=letra)
        self.telefone.place(x=100,y=590)

        self.telefone_span = Label(self.janela, text='Telefone inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.telefone_span.place(x=100,y=630)
        self.error_span.append(self.telefone_span)

        Label(self.janela,text='CEP:  ',bg='#D9D9D9',fg=self.cor_letra, font=('Arial',12)).place(x=600,y=560)

        self.cep = Entry(self.janela,width=20,font=letra)
        self.cep.place(x=600,y=590)

        self.cep_span = Label(self.janela, text='CEP inválido', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.cep_span.place(x=600,y=630)
        self.error_span.append(self.cep_span)
        
        Label(self.janela,text='Estado:  ',bg='#D9D9D9',fg=self.cor_letra, font=('Arial',12)).place(x=1100,y=560)

        self.estado = Entry(self.janela,width=10,font=letra)
        self.estado.place(x=1100,y=590)

        self.estado_span = Label(self.janela, text='UF inválida', bg='#D9D9D9', fg='#D9D9D9', font=('Arial',10))
        self.estado_span.place(x=1100,y=630)

        self.borda3 = Frame(self.janela,bg=self.cor_letra,width=328,height=54)
        
        self.confirmaedit = Button(self.janela,width=35,height=2, fg=self.cor_letra,text='Confirmar',font=('Comic',12), command=self.attPaciente)

        self.borda4 = Frame(self.janela,bg=self.cor_letra,width=328,height=54)
        
        self.confirmadelete = Button(self.janela,width=35,height=2, fg=self.cor_letra,text='Excluir',font=('Comic',12), command=self.deletePaciente)
        
        self.volta = Button(self.janela,text='<- Página inicial ',command=self.voltar)
        self.volta.place(x=40,y=750)

    
    def voltar(self):
        self.janela.destroy()
        index.Projeto()

    def adiconaPaciente(self):
        self.borda3.place_forget()
        self.confirmaedit.place_forget()

        self.borda4.place_forget()
        self.confirmadelete.place_forget()

        self.ok = 0
        self.lista_pacientes = []
        self.paci_nome = self.nome.get()

        self.paci_cpf = self.cpf.get()
        self.lista_pacientes.append(self.paci_cpf)

        self.paci_sus = self.sus.get()
        self.lista_pacientes.append(self.paci_sus)

        self.paci_idade = self.idade.get()
        self.lista_pacientes.append(self.paci_idade)

        self.paci_telefone = self.telefone.get()
        self.lista_pacientes.append(self.paci_telefone)

        self.paci_cep = self.cep.get()
        self.lista_pacientes.append(self.paci_cep)

        self.paci_uf = self.estado.get()

        if(self.paci_nome == '' or self.paci_nome.isnumeric()):
            self.nome_span.configure(fg = self.cor_letra, text='Nome inválido')
        else:
            self.nome_span.configure(text='')
            self.ok += 1

        if(self.paci_uf == '' or self.paci_uf.isnumeric()):
            self.estado_span.configure(fg = self.cor_letra)
        else:
            self.estado_span.configure(fg = '#D9D9D9')
            self.ok += 1

        for i in range(len(self.lista_pacientes)):
            try:
                if(self.lista_pacientes[i].isnumeric() != True):
                    print(1/0)
            except ZeroDivisionError:
                self.error_span[i].configure(fg = self.cor_letra)
            else:
                self.error_span[i].configure(fg = '#D9D9D9')
                self.ok += 1

        if(self.ok == 7):
            con = sqlite3.connect('Banco_principal.db')
            sql = con.cursor()
            sql.execute("""INSERT INTO PACIENTES (nome, cpf, sus, idade, telefone, cep, uf)
                        VALUES (?,?,?,?,?,?,?)""", (self.paci_nome, self.paci_cpf, self.paci_sus,
                        self.paci_idade, self.paci_telefone, self.paci_cep, self.paci_uf))
            con.commit()
            con.close()

            self.nome.delete(0, END)
            self.cpf.delete(0, END)
            self.sus.delete(0, END)
            self.idade.delete(0, END)
            self.telefone.delete(0, END)
            self.cep.delete(0, END)
            self.estado.delete(0, END)

            self.nome_span.configure(text='Paciente cadastrado', fg = self.cor_letra)
            self.estado_span.configure(fg = '#D9D9D9')
            for i in range(len(self.lista_pacientes)):
                self.error_span[i].configure(fg = '#D9D9D9')

    def editarPaciente(self):
        self.att_paci_nome = self.nome.get()
        self.att_cpf = self.cpf.get()

        #Apaga os spans 
        self.nome_span.configure(text = '')
        self.estado_span.configure(text = '')
        for i in range(len(self.error_span)):
            self.error_span[i].configure(fg = '#D9D9D9')

        if(self.nome.get() == '' or self.cpf.get() == ''):
            self.nome_span.configure(fg = self.cor_letra, text='Digite um nome e cpf para editar')
        else:
            con = sqlite3.connect('Banco_principal.db')
            sql = con.cursor()

            self.cadastro = sql.execute(f"SELECT count(nome) FROM PACIENTES WHERE nome = ? AND cpf = ?", (self.nome.get(), self.cpf.get()))
            self.resultado = self.cadastro.fetchone()

            if self.resultado[0] < 1:
                self.nome_span.configure(fg = self.cor_letra, text= 'Paciente não cadastrado')
                con.close()

            else:
                #Aparece os botões confirmar & deletar
                self.borda3.place(x=400,y=690)
                self.confirmaedit.place(x=402, y=692)

                self.borda4.place(x=750,y=690)
                self.confirmadelete.place(x=752, y=692)
                #----------------------------------------

                self.nome_span.configure(fg = '#D9D9D9', text='')
                self.cadastro = sql.execute("SELECT * FROM PACIENTES WHERE nome = ? AND cpf = ? ", (self.nome.get(), self.cpf.get()))
                self.resultado = self.cadastro.fetchone()

                self.sus.delete(0, END)
                self.idade.delete(0, END)
                self.telefone.delete(0, END)
                self.cep.delete(0, END)
                self.estado.delete(0, END)

                self.sus.insert(0, self.resultado[2])
                self.idade.insert(0, self.resultado[3])
                self.telefone.insert(0, self.resultado[4])
                self.cep.insert(0, self.resultado[5])
                self.estado.insert(0, self.resultado[6])
                con.close()
    
    def attPaciente(self):
        con = sqlite3.connect('Banco_principal.db')
        sql = con.cursor()

        sql.execute("UPDATE PACIENTES SET nome = ?, cpf = ?, sus = ?, idade = ?, telefone = ?, cep = ?, uf = ? WHERE nome = ? AND cpf = ?",
                    (self.nome.get(), self.cpf.get(), self.sus.get(), self.idade.get(), self.telefone.get(),
                    self.cep.get(), self.estado.get(), self.att_paci_nome, self.att_cpf)) 
        con.commit()
        con.close()

        self.nome.delete(0, END)
        self.cpf.delete(0, END)
        self.sus.delete(0, END)
        self.idade.delete(0, END)
        self.telefone.delete(0, END)
        self.cep.delete(0, END)
        self.estado.delete(0, END)

        self.nome_span.configure(fg= self.cor_letra, text = "Cadastro atualizado com sucesso")

        self.borda3.place_forget()
        self.confirmaedit.place_forget()

        self.borda4.place_forget()
        self.confirmadelete.place_forget()
    
    def deletePaciente(self):
        
        #Pega o cpf e se for vazio, retorna aviso
        if(self.cpf.get() == ''):
            self.nome_span.configure(fg = self.cor_letra, text='Digite um CPF cadastrado para excluir')
        else:
        #Abre o BD
            con = sqlite3.connect('Banco_principal.db')
            sql = con.cursor()
        #Confere se o cadastro existe
            self.cadastro = sql.execute(f"SELECT count(cpf) FROM PACIENTES WHERE nome = ? AND cpf = ? ", (self.nome.get(), self.cpf.get()))
            self.resultado = self.cadastro.fetchone()

            if self.resultado[0] < 1:
                #Não existe, retorna erro
                self.cpf_span.configure(fg = self.cor_letra, text= 'Nome/CPF não cadastrado')

            else:
                #Criando a janela2
                self.janela2 = Tk()
                self.janela2.configure(bg='white')
                self.janela2.geometry("{0}x{1}+0+0".format(trunc(self.janela2.winfo_screenwidth()/5), trunc(self.janela2.winfo_screenheight()/5)))

                self.confirma = Frame(self.janela2, width=40,height=10, bg='white')
                self.confirma.place(x=50,y=50)
                Label(self.janela2, text='Deseja mesmo excluir?', bg='white', fg= 'blue').place(x=85,y=25)
                self.botaoConfirmar = Button(self.janela2, text='Confirmar', bg='blue',fg='white', command = self.excluir)
                self.botaoConfirmar.place(x=85, y=82)
                self.botaoCancela =  Button(self.janela2, text='Cancelar',bg='blue',fg='white', command = self.cancelar)
                self.botaoCancela.place(x=155, y=82)

            con.close()
                    

    def excluir(self):
        #Remove a janela2
        self.janela2.destroy()

        #abre o BD e deleta o valor
        con = sqlite3.connect('Banco_principal.db')
        sql = con.cursor()
        sql.execute("DELETE FROM PACIENTES WHERE nome = ? AND cpf = ?", (self.nome.get(), self.cpf.get())) 

        #Apaga os campos de input e notifica sucesso
        self.nome.delete(0, END)
        self.cpf.delete(0, END)
        self.sus.delete(0, END)
        self.idade.delete(0, END)
        self.telefone.delete(0, END)
        self.cep.delete(0, END)
        self.estado.delete(0, END)

        self.nome_span.configure(fg= self.cor_letra, text="Cadastro Excluído")

        #Remove os botões de confirmar e excluir e fecha o BD
        self.borda3.place_forget()
        self.confirmaedit.place_forget()

        self.borda4.place_forget()
        self.confirmadelete.place_forget()

        con.commit()
        con.close()

    def cancelar(self):
        self.janela2.destroy()