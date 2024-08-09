# Função para calcular a área de um pentágono
def pentagono(lado, apotema):  # apotema é a altura do pentágono
    area = (5 * lado * apotema) / 2
    return area

# Teste para a função pentagono
print(pentagono(6, 8))  # Resultado esperado: 120.0
print(pentagono(5, 7))  # Resultado esperado: 87.5

