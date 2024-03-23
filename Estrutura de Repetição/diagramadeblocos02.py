# Imprime uma mensagem indicando o início do programa
print('INICIO DO PROGRAMA!')

# Inicializa a variável 'resp' com o valor "sim"
resp = "sim"

# Inicia um loop que continua enquanto a variável 'resp' for igual a "sim"
while resp == "sim":
    # Solicita ao usuário que insira um número qualquer e o converte para float
    num = float(input('digite um numero qualquer:'))
    
    # Multiplica o número inserido pelo usuário por 3 e atribui o resultado à variável 'r'
    r = num * 3
    
    # Imprime o resultado da multiplicação
    print(r)
    
    # Solicita ao usuário se deseja continuar e armazena a resposta em 'resp'
    resp = input('deseja continuar?:')
    
    # Se a resposta não for "sim", o loop é quebrado
    if resp != "sim":
        break

# Imprime uma mensagem indicando o fim do programa
print('FIM DO PROGRAMA!')
