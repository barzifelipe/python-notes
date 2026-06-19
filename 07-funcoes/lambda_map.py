numeros = [1, 2, 3, 4, 5]

quadrados = list(
    map(
        lambda numero: numero ** 2,
        numeros
    )
)

print(quadrados)


nomes = ["ana", "bruno", "carlos"]

nomes_maisculos = list(
    map(
        lambda nome: nome.upper(),
        nomes
    )
)

print(nomes_maisculos)