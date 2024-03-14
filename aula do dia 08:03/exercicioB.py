'''num = int(input("digite um numero: "))  # Solicita ao usuário que digite um número e o converte para inteiro

i = 1  # Inicializa a variável de controle do loop

while i <= 100:  # Executa o loop enquanto i for menor ou igual a 10
    resultado = num * i  # Calcula o resultado da multiplicação entre num e i
    print(f"{num} x {i} = {resultado}")  # Imprime a multiplicação no formato "num x i = resultado"
    i += 1  # Incrementa o valor de i em 1 a cada iteração do loop'''
#usando for em vez de while
num = int(input("digite um numero: "))  # Solicita ao usuário que digite um número e o converte para inteiro
for i in range(1, 101):
    resultado = num * i  # Calcula o resultado da multiplicação entre num e i
    print(f"{num} x {i} = {resultado}")  # Imprime a multiplicação no formato "num x i = resultado"
    i += 1  # Incrementa o valor de i em 1 a cada iteração do looop