import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

cursor= conexao.cursor()
print("=/" * 50)
print("3) Selecionar todos os registros do ensino “fundamental”")


elementary_school = "SELECT * FROM `ideb` WHERE ensino = 'fundamental'"
cursor.execute(elementary_school)

cont = 0
registros = cursor.fetchall()

for linha in registros:
    print("-=" * 50)
    cont += 1
    print(f"Resgistros do ensino fundamental", linha)

print("=" * 50)    
print(f"Foram encontrados", cont, "registros de ensino fundamental")
print("=" * 50)

conexao.close()