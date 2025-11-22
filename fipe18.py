from database import get_connection

conexao = get_connection()

cursor= conexao.cursor()
print("=/" * 50)
print("18) Selecionar todos os veículos que tenham o ano de fabricação entre 2000 e 2018, ordenados por ano de forma crescente.")

select = "SELECT * FROM `fp_ano` WHERE `valor` BETWEEN 20000 AND 1000000;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)



conexao.close()