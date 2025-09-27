import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

cursor= conexao.cursor()

print("=/" * 0)
print("7) Selecione o maior valor para “nota_saeb_matematica”")

highest_grade = "SELECT nota_saeb_matematica FROM `ideb`;"
cursor.execute(highest_grade)

maior = 0
registros = cursor.fetchall()

for linha in registros:
    
    result = linha[0]
    if result > maior:
        maior = result
    print(f"Registros das notas do campo 'nota_saeb_matematica'", linha)


print("=" * 80)    
print(f"A maior nota do campo 'nota_saeb_matematica' é: {maior:.2f}")
print("=" * 80)

conexao.close()