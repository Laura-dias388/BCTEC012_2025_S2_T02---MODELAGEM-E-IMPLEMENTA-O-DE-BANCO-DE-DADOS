from database import get_connection

conexao = get_connection()

cursor= conexao.cursor()
print("=/" * 50)
print("19) Selecionar todos os veículos que tenham o valor menor que R$20.000 entre os anos de 1990 e 2010 ordenados por ano de forma decrescente.")

select = "SELECT * FROM `fp_ano` WHERE `valor` BETWEEN 20000 AND 1000000;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)


conexao.close()