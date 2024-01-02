import sqlite3
 
con = sqlite3.connect('teste.db')
sql = con.cursor()
 
listaTabelas = sql.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='NOMES'")

if listaTabelas.fetchone()[0]!=1 :
    sql.execute("CREATE TABLE NOMES (nome,telefone)")

con.close()