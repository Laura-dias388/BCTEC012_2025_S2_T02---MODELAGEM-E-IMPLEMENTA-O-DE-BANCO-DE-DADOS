import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='test_db'
)

print("=/" * 50)
print("1) Selecionar todos os registros do ano de “2019”")

cursor= conexao.cursor()

year = "SELECT * FROM `nome`"

cursor.execute(year)
cont = 0
registros = cursor.fetchall()
for linha in registros:
    cont += 1
    print("-=" * 50)
    print(f"Registros do ano de 2019", linha)
    
print("=" * 50)    
print(f"Foram encontrados", cont, "registros do ano de 2019")
print("=" * 50) 

conexao.close()