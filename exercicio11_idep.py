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

value_year = "SELECT ano, ideb FROM ideb ORDER BY ideb DESC LIMIT 1"  
# pega apenas o ano e o valor da coluna ideb e ordena em ordem decrescente pegando somente a primeira linha.

cursor.execute(value_year)
maior = 0
registros = cursor.fetchone()

year = registros[0]
greater_value = registros[1]

print(f"O ano em que teve o maior valor para o ideb foi:",year ,"e o valor foi:", greater_value)
print("=" * 50) 

conexao.close()