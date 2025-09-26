import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)
cursor= conexao.cursor()
print("=/" * 80)
print("10) Encontre o valor da média dos valores para o “nota_saeb_media_padronizada”")


average = "SELECT * FROM `ideb` ORDER BY `ideb`.`nota_saeb_media_padronizada` ASC;"
cursor.execute(average)

cont = 0
soma = 0
registros = cursor.fetchall()

for linha in registros:
    print("-=" * 50)
    cont += 1
    result = linha[0]
    soma += result
    print(f"Registros das notas do campo 'nota_saeb_media_padronizada'", linha)

standard_verage = soma / cont

print("=" * 80)    
print(f"A média das notas do campo 'nota_saeb_media_padronizada' é: {standard_verage:.2f}")
print("=" * 80)

conexao.close()