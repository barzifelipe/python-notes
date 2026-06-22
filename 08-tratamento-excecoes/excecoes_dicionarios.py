alunos = {
    "Felipe": [7, 8, 9],
    "Maria": [6, 4 ,7],
    "Rafael": [8, 8, 10]
}

try: 
    nome = input("Digite o nome do aluno: ")
    resultado = alunos[nome]

except KeyError:
    print("Aluno não encontrado")

else:
    print(resultado)