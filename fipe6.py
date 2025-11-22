from database import get_connection

conexao = get_connection()

cursor= conexao.cursor()
print("=/" * 50)
print("6) Contar quantos registros existem para o ano 2015")

select = "SELECT COUNT(*) FROM `fp_ano` WHERE ano = 2015;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)



conexao.close()