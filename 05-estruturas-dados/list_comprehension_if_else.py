notas = [8, 5, 9, 6, 4]

situacao = [
    "Aprovado" if nota >= 7 else "Reprovado"
    for nota in notas
]

print(situacao)