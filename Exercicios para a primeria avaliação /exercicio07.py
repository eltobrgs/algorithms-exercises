'''Escreva um programa que leia o índice pluviométrico de cada dia do mês de
junho e informe o dia que mais choveu, o dia que menos choveu e as médias
pluviométricas de cada uma das duas quinzenas.'''

dias = 5
pluvio = []
for i in range(dias):
    pluvio.append(float(input(f"Digite a pluviosidade do dia {i + 1}: "))
)
print(f"O dia que mais choveu foi o dia {pluvio.index(max(pluvio)) + 1} com {max(pluvio)}mm")