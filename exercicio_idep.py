import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

cursor= conexao.cursor()
comando = "SELECT * FROM ideb WHERE ano = 2019;"

cursor.execute(comando)
registros = cursor.fetchall()
for linha in registros:
    print(linha)

conexao.commit()
conexao.close()