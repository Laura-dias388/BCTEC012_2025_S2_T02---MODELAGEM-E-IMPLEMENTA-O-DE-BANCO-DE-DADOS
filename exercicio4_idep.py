import mysql.connector

conexao = mysql.connector.connect(

   host='localhost',
   user='root',
   password='',
   database='idep_bd'
)
cursor= conexao.cursor()

print("=/" * 80)
print("4) Selecionar todos os registros em que o “anos_escolares” seja igual a “finais (6-9)”")

school_year = "SELECT * FROM `ideb` WHERE RIGHT(ano, 1) IN ('6','7','8','9')"
cursor.execute(school_year)

cont = 0
registros = cursor.fetchall()

for linha in registros:
    print("-=" * 50)
    cont += 1
    print(f"Resgistros do ano escolar com finais 6-9", linha)

print("=" * 50)    
print(f"Foram encontrados", cont, "registros de ano escolar entre 6-9")
print("=" * 50)

conexao.close()