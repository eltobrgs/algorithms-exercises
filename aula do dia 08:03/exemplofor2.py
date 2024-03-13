# Imprime uma mensagem indicando o início do programa
print('INICIO DO PROGRAMA!')

# Inicializa a variável 'contador' com o valor 1
contador = 1

# Utilizando um loop 'for' para iterar sobre uma sequência de números de 1 a 5 (inclusive)
# O valor final (6) não está incluso na sequência
for contador in range(1, 6):
    # Solicita ao usuário que insira um número e o converte para inteiro
    x = int(input('digite um valor qualquer: '))
    
    # Calcula o resultado multiplicando o número inserido pelo usuário por 3
    r = x * 3
    
    # Imprime o resultado da multiplicação
    print(r)

# Imprime uma mensagem indicando o fim do programa
print('FIM DO PROGRAMA!')



#A estrutura for em Python não exige que você incremente manualmente o contador, como é necessário em um loop while. 
#O for itera automaticamente sobre os itens de uma sequência (como uma lista, tupla, string, etc.) 
#e não requer a atualização explícita de uma variável de controle.

#Portanto, no código fornecido, a linha contador = 1 é inicializada, mas não tem efeito sobre o loop for,
# uma vez que o próprio for gerencia a iteração. O range(1, 6) gera uma sequência de números de 1 a 5 (inclusive), 
#e o for itera automaticamente sobre essa sequência sem necessidade de atualização manual do contador.