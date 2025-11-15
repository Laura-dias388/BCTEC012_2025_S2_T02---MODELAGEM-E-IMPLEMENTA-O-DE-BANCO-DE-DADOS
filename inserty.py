import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="assistencia_autorizada_db"
)

cursor = conexao.cursor()

dados1 = [
  (1, "Marco", "Trainee"),
  (2, "Hélio", "Sênior"),
  (3, "Tião", "Sênior"),
  (4, "Sílvio", "Estagiário")
]
query = "INSERT INTO FUNCIONARIO (NumFunc, Nome, Cargo) VALUES (%s, %s, %s)"
cursor.executemany(query, dados1)

dados_aparelho = [
    (1, 3, 5, "Pedro"),
    (2, 4, 7, "Carlos"),
    (3, 4, 3, "Paulo"),
    (4, 5, 1, "Ramos"),
    (5, 1, 10, "Paulo"),
    (6, 2, 12, "Paulo"),
    (7, 4, 9, "Alice"),
    (9, 3, 7, "Maria"),
    (10, 1, 3, "Pedro"),
    (11, 1, 7, "José")
]

query = "INSERT INTO APARELHO (NumAp, Tipo, Idade, Dono) VALUES (%s, %s, %s, %s)"

cursor.executemany(query, dados_aparelho)

dados_experiencia = [
    (2, 2, 15),
    (3, 1, 18),
    (1, 3, 1),
    (1, 2, 1),
    (4, 1, 5),
    (2, 4, 12),
    (3, 5, 14),
    (3, 4, 10),
    (3, 2, 12)
]

query = "INSERT INTO EXPERIENCIA (NumFuncionario, Tipo, AnosExperiencia) VALUES (%s, %s, %s)"

cursor.executemany(query, dados_experiencia)

dados_conserto = [
    (1, 1),
    (2, 10),
    (3, 11),
    (2, 1),
    (2, 5),
    (3, 6),
    (2, 7),
    (1, 8)
]

query = "INSERT INTO CONSERTO (NumFunc, NumAp) VALUES (%s, %s)"

cursor.executemany(query, dados_conserto)

conexao.commit()

cursor.close()
conexao.close()

print("Inserido com sucesso!")
