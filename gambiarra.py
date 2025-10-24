import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",       
    user='root',            
    password='',
    database='assistencia_tecnica_gambiarra_db',
)

cursor = conexao.cursor()

cursor.execute("CREATE TABLE Funcionario "
"(NumFunc INT PRIMARY KEY AUTO_INCREMENT," \
" Nome VARCHAR(100) NOT NULL, Cargo VARCHAR(50)," \
" AnosExperiencia INT)"
)
cursor.execute("CREATE TABLE Tipo "
"(IdTipo INT PRIMARY KEY AUTO_INCREMENT," \
" Tipo VARCHAR(50) NOT NULL, Categoria VARCHAR(50)," \
" Taxa DECIMAL(10,2)"
)
cursor.execute("CREATE TABLE Aparelho"
" (NumAp INT PRIMARY KEY AUTO_INCREMENT," \
" Idade INT, Dono VARCHAR(100), IdTipo INT," \
" FOREIGN KEY (IdTipo) REFERENCES Tipo(IdTipo)"
)
cursor.execute("CREATE TABLE Experiencia"
" (NumFunc INT, IdTipo INT," \
" PRIMARY KEY (NumFunc, IdTipo)," \
" FOREIGN KEY (NumFunc) REFERENCES Funcionario(NumFunc)," \
" FOREIGN KEY (IdTipo) REFERENCES Tipo(IdTipo)"
)
cursor.execute("CREATE TABLE Conserto"
" (NumFunc INT," \
" NumAp INT," \
" PRIMARY KEY (NumFunc, NumAp)," \
" FOREIGN KEY (NumFunc) REFERENCES Funcionario(NumFunc)," \
" FOREIGN KEY (NumAp) REFERENCES Aparelho(NumAp)"
)

cursor.close()
conexao.close()
