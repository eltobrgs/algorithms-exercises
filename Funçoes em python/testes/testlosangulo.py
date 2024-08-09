
# Função para calcular a área de um losango
def losango(diagonal_maior, diagonal_menor):
    area = (diagonal_maior * diagonal_menor) / 2
    return area

# Teste para a função losango
print(losango(10, 6))  # Resultado esperado: 30.0
print(losango(8, 5))   # Resultado esperado: 20.0