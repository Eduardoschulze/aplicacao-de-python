#importa a biblioteca
# serve para conectar o banco de dados ao python
import mysql.connector

#executa função de lib (biblioteca)
conexao = mysql.connector.connect(
    #parametros de conexao de banco de dados
    host = "localhost",
    user = "root",
    password = "",
    database = "oficinagit"
)

print ("conectado")


#funcao cursor () da lib
#serve para manipular os dados de envio para banco de dados
cursor = conexao.cursor()


sql = "INSERT INTO funcionarios(cpf,nome,especialidade,telefone) VALUES (%s, %s, %s, %s)"
values = ("1129", "Pedrinho", "mecanico", "499914185")

cursor.execute(sql, values)
conexao.commit()

cursor.execute("SELECT * FROM funcionarios")
resultado = cursor.fetchall()

for i in resultado:
    print(i)
