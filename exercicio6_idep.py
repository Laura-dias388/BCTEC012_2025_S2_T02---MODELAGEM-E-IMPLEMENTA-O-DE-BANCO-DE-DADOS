import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)
cursor= conexao.cursor()

print("=/" * 80)
print("6) Encontre o valor da média dos valores para o “indicador_rendimento”")

yield_indicator = "SELECT indicador_rendimento FROM `ideb`;"
cursor.execute(yield_indicator)

cont = 0
soma = 0
registros = cursor.fetchall()

for linha in registros:
    print("-=" * 50)
    cont += 1
    result = linha[0]
    soma += result
    print(f"Registros de valores das taxas de aprovação", linha)

average = soma / cont

print("=" * 80)    
print(f"A média dos valores para o campo 'indicador_redimento' é: {average:.2f}")
print("=" * 80)

conexao.close()