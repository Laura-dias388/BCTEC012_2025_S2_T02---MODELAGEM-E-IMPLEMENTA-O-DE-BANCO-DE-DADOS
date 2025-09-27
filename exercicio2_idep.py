import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

print("=/" * 50)
print("2) Selecionar todos os registros da rede “privada”")

cursor= conexao.cursor()
private_network = "SELECT * FROM `ideb` WHERE rede = 'privada'"

cursor.execute(private_network)
cont = 0
registros = cursor.fetchall()

for linha in registros:
    print("-=" * 50)
    cont += 1
    print(f"Resgistros de rede privada", linha)

print("=" * 50)    
print(f"Foram encontrados", cont, "resgistros de rede privada")
print("=" * 50)

conexao.close()