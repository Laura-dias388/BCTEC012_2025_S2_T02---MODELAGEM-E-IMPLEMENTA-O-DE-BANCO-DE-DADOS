
import mysql.connector


conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='aula_pratica_1'
)

cursor= conexao.cursor()
nome='Maria'
cpf='078.779.789-45'
endereco= 'Raua c'
cidade = 'bh'
numero=20

#comando= f'select * from cliente'
comando= f'insert into cliente (nome, cpf, endereco, cidade, numero) values ("{nome}", "{cpf}", "{endereco}", "{cidade}", {numero})'

cursor.execute(comando)
conexao.commit()

#resultado = cursor.fetchall()

#for cliente in resultado:
#    print(cliente)

conexao.close()
