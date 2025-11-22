from database import get_connection

conexao = get_connection()
cursor = conexao.cursor()

print("=/" * 50)
print("3) Selecionar todos os anos que o combustível seja gasolina e que o valor seja menor que 50.000")

select = "SELECT ano FROM `fp_ano` WHERE `valor` < 50000 AND `combustivel` = 'gasolina';"
cursor.execute(select)

registros = cursor.fetchall()
cont = 0

for linha in registros:
    print("-=" * 50)
    cont += 1
    
    print(f"Registros de {cont} anos onde o combustível é gasolina e o valor menor que 50 mil.", linha)



conexao.close()