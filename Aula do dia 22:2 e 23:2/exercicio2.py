# Desenvolva um programa que efetue o cálculo da área de uma circunferência,
# apresentando a medida calculada

pi = 3.14
r = float(input('Digite o valor do raio da circunferência:'))

area = pi * (r ** 2)

print(f"Se o raio da circunferência for {r}, a área será {area:.1f}")