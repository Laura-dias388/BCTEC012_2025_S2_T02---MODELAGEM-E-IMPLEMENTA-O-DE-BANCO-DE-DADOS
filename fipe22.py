from database import get_connection

conexao = get_connection()

cursor= conexao.cursor()
print("=/" * 50)
print("22) Selecionar o menor valor dos veículos da marca “SSANGYONG” que sejam do ano de 2018.")

select = "SELECT * FROM `fp_ano` WHERE `valor` BETWEEN 20000 AND 1000000;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)



conexao.close()