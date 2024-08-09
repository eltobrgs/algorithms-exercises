# Função para calcular área e perímetro de um retângulo
def retangulo(lado1, lado2):
    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)
    return area, perimetro

# Teste para a função retangulo
print(retangulo(5, 10))  # Resultado esperado: (50, 30)
print(retangulo(3, 4))   # Resultado esperado: (12, 14)
