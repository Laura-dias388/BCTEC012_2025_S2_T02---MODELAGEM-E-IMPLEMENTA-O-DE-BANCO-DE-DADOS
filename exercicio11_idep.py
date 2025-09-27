import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

cursor= conexao.cursor()
print("=/" * 50)
print("11) Encontre o ano que teve o maior valor para o ideb")

value_year = "SELECT ano, ideb FROM ideb WHERE ideb = (SELECT MAX(ideb) FROM ideb);"  
# pega apenas o ano e o valor da tabela ideb .

cursor.execute(value_year)

registros = cursor.fetchall()

for reg in registros:
  print(f"O ano em que teve o maior valor para o ideb foi:",reg)
print("=" * 50) 

conexao.close()