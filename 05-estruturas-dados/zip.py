nomes = ["Ana", "Bruno", "Carlos"]
notas = [8.5, 7.0, 9.4]

alunos = list(zip(nomes, notas))

print(alunos)

# A função zip cria uma lista de tuplas
# Se quisesse criar uma lista de listas seria assim: 

resultado = ([nome, nota] for nome, nota in zip(nomes, notas))

print(resultado)