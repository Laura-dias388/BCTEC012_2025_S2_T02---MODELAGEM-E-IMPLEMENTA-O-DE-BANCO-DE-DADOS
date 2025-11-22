from database import get_connection

conexao = get_connection()
cursor= conexao.cursor()
print("=/" * 50)
print("9) Mostrar todos os tipos de combustível cadastrados")

select = "SELECT * FROM `fp_ano` WHERE `valor` BETWEEN 20000 AND 1000000;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)



conexao.close()