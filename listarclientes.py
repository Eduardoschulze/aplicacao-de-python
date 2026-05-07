import mysql.connector
from conexao import conectar

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