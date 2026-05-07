import mysql.connector
from conexao import conectar

def inserir_dados():

    nome = input ("qual seu nome? ")
    cpf = input("qual seu cpf ? ")
    idade = input ("qual sua idade")
    genero = ("qual seu genero?")
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        sql = "INSERT INTO pessoas (nome, cpf, idade, genero) VALUES (%s, %s, %s, %s)"
        values = (nome,cpf,idade,genero)

        cursor.execute(sql, values)
        conexao.commit()

        print("cliente inserido")

        cursor.close()
        conexao.close()