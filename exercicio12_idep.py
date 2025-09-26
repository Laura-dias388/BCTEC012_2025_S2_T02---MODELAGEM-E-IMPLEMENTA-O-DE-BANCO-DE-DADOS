import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)
cursor= conexao.cursor()
print("=/" * 80)
print("12) Encontre os maiores valores para “projecao” para cada tipo de rede")


projection_value = "SELECT rede, MAX(projecao) FROM ideb GROUP BY rede;"
# da tabela ideb o MySQL pega todos os dados e agrupa pelos valores da coluna rede, dentro de cada grupo ele pega o maior valor da projeção

cursor.execute(projection_value)

registros = cursor.fetchall()

for rede, projecao in registros:
    print("=" * 30)
    print(f"{rede}")
    print(f"Maior projeção: {projecao}")
    print("=" * 30)
    
conexao.close()