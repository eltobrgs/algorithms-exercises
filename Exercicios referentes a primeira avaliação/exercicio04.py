# Define o alfabeto como uma lista de letras minúsculas
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Solicita ao usuário que digite uma mensagem
mensagem = input("Digite uma mensagem: ")

# Solicita ao usuário que digite um número inteiro
chave = int(input("Digite um número inteiro: "))

# Inicializa uma string vazia para armazenar a mensagem criptografada
mensagem_criptografada = ''

# Itera sobre cada letra na mensagem
for letra in mensagem:
    # Inicializa variáveis para a busca binária
    inicio = 0
    fim = len(alfabeto) - 1
    meio = (inicio + fim) // 2
    
    # Realiza a busca binária para encontrar o índice da letra no alfabeto
    while inicio <= fim and alfabeto[meio] != letra:
        if letra < alfabeto[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
        meio = (inicio + fim) // 2

    # Se a letra for encontrada no alfabeto
    if alfabeto[meio] == letra:
        # Calcula o código criptografado adicionando a chave
        codigo = meio + chave
        
        # Volta para o início do alfabeto, se necessário
        if codigo > 25:
            codigo = codigo - 26
        
        # Adiciona a letra criptografada à mensagem criptografada
        mensagem_criptografada += alfabeto[codigo]

# Imprime a mensagem criptografada
print(mensagem_criptografada, "mensagem criptografada")