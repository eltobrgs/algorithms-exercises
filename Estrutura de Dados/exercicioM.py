a=[]
num = int(input("digite um numero: "))  # Solicita ao usuário que digite um número e o converte para inteiro
for i in range(1, 11):
    resultado = num * i  # Calcula o resultado da multiplicação entre num e i
    a.append(resultado)
    print(f"{num} x {i} = {resultado}")  # Imprime a multiplicação no formato "num x i = resultado"
    i += 1  # Incrementa o valor de i em 1 a cada iteração do looop
print(f'os resultados da tabuada sao respectivamnete {a}')
