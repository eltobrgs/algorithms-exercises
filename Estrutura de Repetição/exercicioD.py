# Iterar através dos números de 1 a 500
for contador in range(1, 501):
    # Verificar se o número é par
    if contador % 2 == 0:
        somatorio = 0  # Inicializar a variável de soma
        # Iterar através dos números de 1 até o número atual (inclusive)
        for j in range(1, contador+1):
            somatorio += j  # Adicionar cada número à soma
        # Imprimir a soma dos números
        print(f"somatório do número {contador} é {somatorio}")

# Imprimir a mensagem de fim do programa
print("Fim do programa")