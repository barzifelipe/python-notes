try: 
    numero = input("Digite um número: ")

except ValueError:
    print("Digite apenas números inteiros")

else:
        print(f"Número digitado {numero}")