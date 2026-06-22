try:
    numero = int("abc")

except ValueError:
    print("ValueError: valor inválido para a conversão")

try:
    resultado = 10 / 0

except ZeroDivisionError:
    print("ZeroDivisionError: divisão por zero")

try: 
    lista = [1, 2, 3]
    print(lista[5])

except IndexError:
    print("IndexError: indíce fora da lista")