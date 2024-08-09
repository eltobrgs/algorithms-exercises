# Função para verificar se um número é o menor de uma lista
def eh_o_menor(numero, lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    if numero == menor:
        return True
    else:
        return False
    

# Teste para a função eh_o_menor
print(eh_o_menor(1, [1, 5, 10]))  # Resultado esperado: True
print(eh_o_menor(5, [1, 5, 10]))  # Resultado esperado: False
