def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    
    return saldo - valor

try:
    saldo = sacar(100, 150)
except ValueError as erro:
    print(erro)