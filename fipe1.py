from database import get_connection

conexao = get_connection()
cursor = conexao.cursor()

print("=/" * 50)
print("1) Selecionar todos os anos que sejam maior ou igual a 2000”")

select = "SELECT ano FROM `fp_ano` WHERE `ano` >= 2000;"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(f"Registros de {cont} anos maiores que 2000'", linha)



conexao.close()