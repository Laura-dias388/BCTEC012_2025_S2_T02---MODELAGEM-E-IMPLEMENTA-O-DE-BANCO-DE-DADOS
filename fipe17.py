from database import get_connection

conexao = get_connection()

cursor= conexao.cursor()
print("=/" * 50)
print("""17) Selecionar todos os veículos que tenham o combustível gasolina
e que tenha o ano entre 2000 e 2015 e que o valor seja menor que 50.000 ordenados por ordem alfabética do modelo do veículo.""")

select = "SELECT * FROM `fp_ano` WHERE `valor` BETWEEN 20000 AND 1000000;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(linha)


conexao.close()