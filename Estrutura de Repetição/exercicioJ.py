#usando for 
'''# Temperaturas inicial e final em Celsius
temperatura_inicial = 10
temperatura_final = 100

# Percorra as temperaturas e converta
for celsius in range(temperatura_inicial, temperatura_final + 10, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit")'''
#usando while

# Definindo a temperatura inicial e final em Celsius
temperatura_inicial = 10
temperatura_final = 100

# Inicializando a variável celsius com a temperatura inicial
celsius = temperatura_inicial

# Enquanto a temperatura em Celsius for menor ou igual à temperatura final
while celsius <= temperatura_final:
    # Convertendo a temperatura de Celsius para Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    # Imprimindo a temperatura em Celsius e Fahrenheit
    print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit")
    # Incrementando a temperatura em 10 graus Celsius
    celsius += 10