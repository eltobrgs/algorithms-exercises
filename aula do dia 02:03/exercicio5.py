# Ler quatro valores inteiros
valor1 = int(input("Digite o 1º valor inteiro: "))
valor2 = int(input("Digite o 2º valor inteiro: "))
valor3 = int(input("Digite o 3º valor inteiro: "))
valor4 = int(input("Digite o 4º valor inteiro: "))

# Verificar os valores divisíveis por 2 e 3
if valor1 % 2 == 0 and valor1 % 3 == 0:
    print(valor1, "é divisível por 2 e 3")
else:
    print(valor1, 'nao é divisivel nem por 2 e nem por 3')

if valor2 % 2 == 0 and valor2 % 3 == 0:
    print(valor2, " é divisível por 2 e 3")
else:
    print(valor2, 'nao é divisivel nem por 2 e nem por 3')

if valor3 % 2 == 0 and valor3 % 3 == 0:
    print(valor3, " é divisível por 2 e 3")
else:
    print(valor3, 'nao é divisivel nem por 2 e nem por 3')

if valor4 % 2 == 0 and valor4 % 3 == 0:
    print(valor4, " é divisível por 2 e 3")
else:
    print(valor4,'nao é divisivel nem por 2 e nem por 3')
