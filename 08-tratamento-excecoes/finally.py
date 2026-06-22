try:
    numero = int(input("Digite um número: "))

except ValueError: 
    print("Valor inválido")

else: 
    print(numero)

finally:
    print("Programa encerrado")