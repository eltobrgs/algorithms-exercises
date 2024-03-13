import math  # Importa o módulo math para usar funções matemáticas

# Definição das operações básicas

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

# Funções para cálculos geométricos

def hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_quadrado(lado):
    return lado**2

def area_retangulo(base, altura):
    return base * altura

def area_circulo(raio):
    return math.pi * raio**2

def circunferencia(raio):
    return 2 * math.pi * raio

# Exibe o menu de opções

print("Calculadora Matemática")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Calcular Hipotenusa")
print("6 - Calcular Área do Triângulo")
print("7 - Calcular Área do Quadrado")
print("8 - Calcular Área do Retângulo")
print("9 - Calcular Área do Círculo")
print("10 - Calcular Circunferência do Círculo")

# Solicita a escolha da operação ao usuário

opcao = int(input("Escolha uma operação (1-10): "))

# Realiza a operação escolhida pelo usuário

if opcao in range(1, 5):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print("Resultado:", soma(num1, num2))
    elif opcao == 2:
        print("Resultado:", subtracao(num1, num2))
    elif opcao == 3:
        print("Resultado:", multiplicacao(num1, num2))
    elif opcao == 4:
        print("Resultado:", divisao(num1, num2))
        
elif opcao == 5:
    cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
    cateto2 = float(input("Digite o comprimento do segundo cateto: "))
    print("Hipotenusa:", hipotenusa(cateto1, cateto2))
elif opcao == 6:
    base = float(input("Digite o comprimento da base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    print("Área do triângulo:", area_triangulo(base, altura))
elif opcao == 7:
    lado = float(input("Digite o comprimento do lado do quadrado: "))
    print("Área do quadrado:", area_quadrado(lado))
elif opcao == 8:
    base = float(input("Digite o comprimento da base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    print("Área do retângulo:", area_retangulo(base, altura))
elif opcao == 9:
    raio = float(input("Digite o raio do círculo: "))
    print("Área do círculo:", area_circulo(raio))
elif opcao == 10:
    raio = float(input("Digite o raio do círculo: "))
    print("Circunferência do círculo:", circunferencia(raio))
else:
    print("Opção inválida.")
