select nome,genero from movies where ano = 2008

select nome from movies where `audiencia` >85

select count(*)  from movies where `audiencia` > 75

select count(*) from movies where genero = "comedy"

select nome from movies where `lucro` > "$10" limit 1 ;

select * from movies where `produtora` like "%Disney%"

select min(`tomate`) from movies

select max(`tomate`) from movies

import mysql.connector

host = "localhost"
user = "root"
password = ""
database = ""


def conectar():
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password="",
        database=""
    )

    if conexao.is_connected():
        print("Conectado ao banco")
        return conexao
    else:
        print("Erro ao conectar")
        return None



def inserir_dados(nome, idade, turno):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        sql = "INSERT INTO funcionarios (nome, idade, turno) VALUES (%s, %s, %s)"
        values = (nome, idade, turno)

        cursor.execute(sql, values)
        conexao.commit()

        print("Funcionário inserido")

        cursor.close()
        conexao.close()



def exibir_dados():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM funcionarios")
        resultados = cursor.fetchall()

        print("\n Funcionários:")

        for id, nome, idade, turno in resultados:
            print(f"ID: {id} | Nome: {nome} | Idade: {idade} | Turno: {turno}")

        cursor.close()
        conexao.close()



inserir_dados("marcos", 26, "noite")
exibir_dados()