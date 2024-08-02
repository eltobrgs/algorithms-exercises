# Função para calcular area e peprimetro de um quadrilatero
def retangulo(lado1, lado2):
    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)
    return area, perimetro

# Função para calcular a área de um círculo
def circulo(raio):
    area = 3.14 * raio ** 2
    return area

# Função para calcular a área de um triângulo
def triangulo(base, altura):
    area = (base * altura) /2
    return area

# Função para calcular a área de um trapézio
def trapezio(base_menor, base_maior, altura):
    area = ((base_menor + base_maior) * altura) / 2
    return area

# Função para calcular a área de um losango
def losango(diagonal_maior, diagonal_menor):
    area = (diagonal_maior * diagonal_menor) / 2
    return area

# Função para calcular a área de um pentagono
def pentagono(lado, apotema):  # apotema é a altura do pentágono
    area = (5 * lado * apotema) / 2
    return area

# Função para calcular a área de um hexagono
def hexagono(lado):
    area = (3 * lado ** 2 * 3 ** 0.5) / 2
    return area