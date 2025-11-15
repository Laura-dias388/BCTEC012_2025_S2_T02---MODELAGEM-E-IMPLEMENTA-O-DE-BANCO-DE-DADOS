import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",       
    user='root',            
    password='',
    database='assistencia_autorizada_db',
)

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS FUNCIONARIO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    NumFunc INT,
    Nome VARCHAR(50),
    Cargo VARCHAR(50)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS APARELHO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    NumAp INT,
    Idade INT,
    Dono VARCHAR(50),
    Tipo VARCHAR(50)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS TIPO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Tipo VARCHAR(50),
    Categoria VARCHAR(50),
    Taxa DECIMAL(10,2)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS EXPERIENCIA (
    id INT AUTO_INCREMENT PRIMARY KEY,
    AnosExperiencia INT,
    FOREIGN KEY (NumFunc) REFERENCES FUNCIONARIO(NumFunc),
    FOREIGN KEY (Tipo) REFERENCES TIPO(id)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CONSERTO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    PRIMARY KEY (NunAp),
    FOREIGN KEY (NumFunc) REFERENCES FUNCIONARIO(NumFunc),
    FOREIGN KEY (NumAp) REFERENCES APARELHO(NumAp)
)""")



conexao.commit()
cursor.close()
conexao.close()