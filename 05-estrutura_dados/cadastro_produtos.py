produtos = [
    {"nome": "Teclado", "preco": 85},
    {"nome": "Mouse", "preco": 70},
    {"nome": "Fone de ouvido", "preco": 55}
]

somaPreco = 0

for produto in produtos:
    print(f"{produto["nome"]} - Preço: {produto["preco"]}")
    somaPreco += produto["preco"]

media = somaPreco/len(produtos)
print(f"A média de preço dos produtos é: {media:.2f}")