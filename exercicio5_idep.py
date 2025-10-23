import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

cursor= conexao.cursor()

print("=/" * 50)
print("5) Selecionar todos os registros em que a taxa_aprovacao sejam maiores que 80.0")

pass_rate = "SELECT * FROM `ideb` WHERE taxa_aprovacao > 80"
cursor.execute(pass_rate)

cont = 0
registros = cursor.fetchall()

for linha in registros:
    print("-=" * 50)
    cont += 1
    print(f"Resgistros em que a taxa de aprovação é maior que 80 pts", linha)

print("=" * 80)    
print(f"Foram encontrados", cont, "onde a taxa de aprovação é maior que 80 pts")
print("=" * 80)

conexao.close()