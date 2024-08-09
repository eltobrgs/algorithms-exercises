
# Função para calcular a área de um trapézio
def trapezio(base_menor, base_maior, altura):
    area = ((base_menor + base_maior) * altura) / 2
    return area

# Teste para a função trapezio
print(trapezio(5, 10, 6))  # Resultado esperado: 45.0
print(trapezio(3, 4, 8))   # Resultado esperado: 28.0