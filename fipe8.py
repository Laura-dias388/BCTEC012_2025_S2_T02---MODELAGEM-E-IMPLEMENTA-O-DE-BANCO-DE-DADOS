from database import get_connection

conexao = get_connection()
cursor = conexao.cursor()
print("=/" * 50)
print("8) Ordenar todos os preços de forma decrescente onde ano for 2016")

select = "SELECT ano, valor FROM `fp_ano` WHERE ano = 2016 ORDER BY valor DESC;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for ano, valor in registros:
    print("-=" * 50)
    cont += 1
    
    print(f"Preço:", {valor}, "Ano:", {ano})



conexao.close()