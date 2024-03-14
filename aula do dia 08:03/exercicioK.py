#usando while
'''# Inicializar variáveis
quadro_atual = 1
graos_totais = 1

# Calcular o somatório dos grãos de trigo
while quadro_atual < 64:
    quadro_atual += 1
    graos_totais *= 2
    graos_totais += 1

# Apresentar o somatório dos grãos de trigo
print(f"O somatório total de grãos de trigo é: {graos_totais}")'''
'''#usando for ao invés de while
total_graos = 0
graos_quadro_anterior = 1

for quadro in range(1, 65):
    total_graos += graos_quadro_anterior
    graos_quadro_anterior *= 2

print("O total de grãos de trigo no tabuleiro de xadrez é:", total_graos)'''

#forma de antonio enzo 
q = 0  # contador para o número de quadrados
g = 1  # quantidade inicial de grãos em um quadrado
total = 0  # contador para o total de grãos

while q < 64:
    q += 1
    total += g
    print(f"No quadrado {q} tem {g} grãos de trigo.")
    g += g

print(f"O somatório dos grãos é: {total}")