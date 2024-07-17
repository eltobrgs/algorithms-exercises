'''Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3%
ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de
2% ao ano, escreva um programa, que imprima o tempo necessário para que a
população do país A ultrapasse a população do país B.'''
pais_a = 5000000
pais_b = 7000000

anos = 0
while pais_a < pais_b:
    pais_a *= 1.03
    pais_b *= 1.02
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B")