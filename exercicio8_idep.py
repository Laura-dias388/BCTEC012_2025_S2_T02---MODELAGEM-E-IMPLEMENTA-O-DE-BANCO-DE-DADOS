import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

cursor= conexao.cursor()
print("=/" * 50)
print("8) Selecione o menor valor para “nota_saeb_lingua_portuguesa”")

minor_note = "SELECT nota_saeb_lingua_portuguesa FROM `ideb`;"
cursor.execute(minor_note)

menor = float('inf') #Em Python, float('inf') representa o conceito de infinito positivo.
registros = cursor.fetchall()

for linha in registros:
    
    result = linha[0]
    if result < menor:
        menor = result
    print(f"Registros das notas do campo 'nota_saeb_lingua_portuguesa'", linha)

print("=" * 80)    
print(f"A menor nota do campo 'nota_saeb_lingua_portuguesa' é: {menor:.2f}")
print("=" * 80)

conexao.close()