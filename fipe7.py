from database import get_connection

conexao = get_connection()

cursor= conexao.cursor()
print("=/" * 50)
print("7) Ordenar todos os anos de forma crescente onde o combustível for gasolina")

select = "SELECT ano FROM `fp_ano` WHERE `combustivel` = 'gasolina' ORDER BY ano ASC;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)



conexao.close()