import mysql.connector
import random 

conexao = mysql.connector.connect(
    host="localhost",       
    user='root',            
    password='',
    database='brasileirao',
)
intervalos = ["0-10", "11-20", "21-30", "31-40", "41-50", 
              "51-60", "61-70", "71-80", "81-90"]
cursor = conexao.cursor()


cursor.execute("SELECT id FROM partida")
partidas = cursor.fetchall()


for partida in partidas:
    id_partida = partida[0]
    gols_casa = random.randint(0, 7)
    gols_visitante = random.randint(0, 7)

    cursor.execute("""
        UPDATE partida
        SET gols_casa = %s, gols_visitante = %s
        WHERE id = %s
    """, (gols_casa, gols_visitante, id_partida))
for partida in partidas:
    id_partida = partida[0]
    for intervalo in intervalos:
        cursor.execute("""
            INSERT INTO estatistica (
                partida_id, intervalo,
                cartoes_amarelos_casa, cartoes_amarelos_visitante,
                cartoes_vermelhos_casa, cartoes_vermelhos_visitante,
                faltas_casa, faltas_visitante,
                escanteios_casa, escanteios_visitante,
                impedimentos_casa, impedimentos_visitante
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            id_partida, intervalo,
            random.randint(0,5), random.randint(0,5),
            random.randint(0,3), random.randint(0,3),
            random.randint(0,58), random.randint(0,58),
            random.randint(0,10), random.randint(0,10),
            random.randint(0,30), random.randint(0,30)
        ))
conexao.commit()
cursor.close()
conexao.close()
print("Gols atualizados com sucesso!")