from database import get_connection

conexao = get_connection()
cursor = conexao.cursor()

print("=/" * 50)
print("5) Retornar a média dos anos em que o combustível for Álcool")

select = "SELECT AVG(ano) FROM `fp_ano` WHERE `combustivel` = 'Alcool';"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(f"Média: {linha[0]}")



conexao.close()