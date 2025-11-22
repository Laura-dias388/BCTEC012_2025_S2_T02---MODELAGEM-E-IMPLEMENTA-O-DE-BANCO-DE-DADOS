from database import get_connection

conexao = get_connection()
cursor = conexao.cursor()

print("=/" * 50)
print("4) Selecionar todos os anos que forem maior que 2000 e o combustível seja Diesel ordenando o resultado por valor em ordem crescente")

select = "SELECT ano FROM `fp_ano` WHERE `ano` > 2000 AND `combustivel` = 'Diesel';"
cursor.execute(select)
# ORDER BY ano ASC deu erro ao retornar os dados
registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)



conexao.close()