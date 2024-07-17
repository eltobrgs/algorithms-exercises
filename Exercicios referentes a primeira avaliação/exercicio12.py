saldo_medio = float(input("Digite o saldo médio do cliente: "))

if saldo_medio <= 200:
    credito = 0
elif saldo_medio <= 400:
    credito = saldo_medio * 0.2
elif saldo_medio <= 600:
    credito = saldo_medio * 0.3
else:
    credito = saldo_medio * 0.4

print("Saldo médio: R$", saldo_medio)
print("Valor do crédito: R$", credito)