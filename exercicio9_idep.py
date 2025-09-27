import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)

cursor= conexao.cursor()
print("=/" * 50)
print("9) Faça uma média dos valores para o “indicador_rendimento”")

yield_indicator = "SELECT AVG(indicador_rendimento) AS media_do_rendimento FROM ideb;"
cursor.execute(yield_indicator)

result = cursor.fetchall()

media = result[0][0]

print("=" * 80)    
print(f"A média dos valores para o campo 'indicador_redimento' é: {media:.2f}")
print("=" * 80)

conexao.close()