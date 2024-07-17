# Definindo o número de dias em junho
dias = 30

# Lista para armazenar os índices pluviométricos de cada dia
pluvio = []

# Loop para ler os índices pluviométricos de cada dia
for i in range(dias):
    pluvio.append(float(input(f"Digite a pluviosidade do dia {i + 1} de junho: ")))

# Encontrando o dia que mais choveu e o dia que menos choveu
max_pluvio = pluvio[0]
min_pluvio = pluvio[0]
dia_mais_chuvoso = 1
dia_menos_chuvoso = 1

for i in range(1, dias):
    if pluvio[i] > max_pluvio:
        max_pluvio = pluvio[i]
        dia_mais_chuvoso = i + 1
    if pluvio[i] < min_pluvio:
        min_pluvio = pluvio[i]
        dia_menos_chuvoso = i + 1

# Calculando as médias pluviométricas das duas quinzenas
soma_primeira_quinzena = 0
soma_segunda_quinzena = 0

for i in range(15):
    soma_primeira_quinzena += pluvio[i]

for i in range(15, dias):
    soma_segunda_quinzena += pluvio[i]

media_primeira_quinzena = soma_primeira_quinzena / 15
media_segunda_quinzena = soma_segunda_quinzena / 15

# Exibindo os resultados
print(f"O dia que mais choveu foi o dia {dia_mais_chuvoso} com {max_pluvio}mm")
print(f"O dia que menos choveu foi o dia {dia_menos_chuvoso} com {min_pluvio}mm")
print(f"Média pluviométrica da primeira quinzena: {media_primeira_quinzena:.2f}mm")
print(f"Média pluviométrica da segunda quinzena: {media_segunda_quinzena:.2f}mm")