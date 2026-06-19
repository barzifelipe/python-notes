def calcular(a,b):
    soma = a + b
    multiplicacao = a*b

    return soma, multiplicacao

def calcular_pacote(a,b):
    return a+b, a*b

a = 7
b =9

resultado = calcular(a, b)
print(resultado)

# Desempacotando múltiplos retornos
soma, multiplicacao = calcular_pacote(a, b)
print(f"Soma: {soma}\nMultiplicação: {multiplicacao}")
