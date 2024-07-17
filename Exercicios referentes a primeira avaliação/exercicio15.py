
# Pergunta a quantidade de Km percorridos
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))

# Pergunta a quantidade de dias pelos quais o carro foi alugado
dias_alugados = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

# Define o preço por dia e por km
preco_por_dia = 90.0
preco_por_km = 0.20

# Calcula o custo total
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

# Exibe o preço total a pagar
print("O preço total a pagar é: R$", custo_total)
