# Imprime uma mensagem indicando o início do programa
print('INICIO DO PROGRAMA')

# Inicializa a variável Contador com o valor 1
Contador = 1

# Inicia um loop enquanto o valor do contador for menor ou igual a 5
while Contador <= 5:
    # Solicita ao usuário que insira um valor qualquer e o converte para float
    num = float(input('digite um valor qualquer:'))
    
    # Multiplica o valor inserido pelo usuário por 3 e atribui o resultado à variável r
    r = num * 3
    
    # Imprime o resultado da multiplicação
    print(r)
    
    # Incrementa o contador em 1 para controlar as iterações do loop
    Contador += 1

# Imprime uma mensagem indicando o fim do programa
print('FIM DO PROGRAMA')
