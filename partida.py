import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",       
    user='root',            
    password='',
    database='',
)

cursor = conexao.cursor()
cursor.close()
conexao.close()