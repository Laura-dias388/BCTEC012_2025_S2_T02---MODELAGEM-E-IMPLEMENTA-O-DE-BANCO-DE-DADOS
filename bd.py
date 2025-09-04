import mysql.connector

conexao = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = '',
  database = 'aula_pratica_1'
)

cursor = conexao.cursor()

comando = f"SELECT * FROM cliente"
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

for cliente in resultado:
  print(cliente[1])

conexao.close()