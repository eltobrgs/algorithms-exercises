# Função para verificar se um número é o maior de uma lista
def eh_o_maior(numero, lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    if numero == maior:
        return True
    else:
        return False