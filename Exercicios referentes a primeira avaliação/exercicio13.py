# Solicita ao usuário as coordenadas dos dois pontos
x1 = float(input("Digite a coordenada x1 do ponto P1: "))
y1 = float(input("Digite a coordenada y1 do ponto P1: "))
x2 = float(input("Digite a coordenada x2 do ponto P2: "))
y2 = float(input("Digite a coordenada y2 do ponto P2: "))

# Calcula a distância entre os pontos usando a fórmula da distância euclidiana
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Exibe a distância calculada
print("A distância entre os pontos P1 e P2 é:", distancia)
