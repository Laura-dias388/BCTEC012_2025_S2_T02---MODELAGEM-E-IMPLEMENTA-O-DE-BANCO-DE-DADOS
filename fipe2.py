from database import get_connection

conexao = get_connection()
cursor = conexao.cursor()

print("=/" * 50)
print("2) Selecionar todos os valores que estejam entre 20.000 e 100.000")

select = "SELECT * FROM `fp_ano` WHERE `valor` BETWEEN 20000 AND 1000000;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(f"Registros de {cont} valores de veículos com valores entre 20 e 100 mil.", linha)



conexao.close()