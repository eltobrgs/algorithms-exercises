# Função para verificar se um número é par
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Função para verificar se um número é ímpar
def eh_impar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False

# Função para calcular o fatorial de um número
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Função para verificar se um número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Função para calcular a soma dos dígitos de um número
def soma_dos_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

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