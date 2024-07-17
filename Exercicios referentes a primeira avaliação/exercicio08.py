# Criando uma lista de duas dimensões usando List Comprehension
lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Imprimindo a diagonal principal da lista
diagonal_principal = [lista[i][i] for i in range(len(lista))]
print(diagonal_principal)