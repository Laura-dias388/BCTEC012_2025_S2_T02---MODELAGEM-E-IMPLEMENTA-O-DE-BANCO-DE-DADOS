import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
   host="127.0.0.1",
   user='root',
   password='',
   database='plantacao_agricola_db',  
)

cursor  = conexao.cursor()
numero_aleatorio = np.linspace(0, 80, 400) # Intervalo de x entre 0 e 80 kg/ha

numeros = [
  {'equacao': 1, 'a': -0.015, 'b': 0.7, 'c': 3},
  {'equacao': 2, 'a': -0.02, 'b': 0.9, 'c': 2.5},
  {'equacao': 3, 'a': -0.012, 'b': 0.65, 'c':2.8},
  {'equacao': 4, 'a': -0.018, 'b': 0.8, 'c':2.2},
  {'equacao': 5, 'a': -0.014, 'b': 0.6, 'c': 3.1},
  {'equacao': 6, 'a': -0.017, 'b': 0.75, 'c': 2.6},
  {'equacao': 7, 'a': -0.016, 'b': 0.77, 'c': 2.7},
  {'equacao': 8, 'a': -0.013, 'b': 0.69, 'c': 2.9},
  {'equacao': 9, 'a': -0.019, 'b': 0.85, 'c': 2.4},
  {'equacao': 10, 'a': -0.02, 'b': 0.8, 'c': 2.3},
]

for n in numeros:
  numero_equacao = n['equacao']

  for x in numero_aleatorio:
    y = n['a'] * x ** 2 + n['b'] * x + n['c']

    comando = "INSERT INTO coordenada (numero_equacao, coordenada_x, coordenada_y) VALUES (%s, %s, %s)"
    valores = (numero_equacao, x, y)
    cursor.execute(comando, valores)


conexao.commit()

  
conexao.close()

