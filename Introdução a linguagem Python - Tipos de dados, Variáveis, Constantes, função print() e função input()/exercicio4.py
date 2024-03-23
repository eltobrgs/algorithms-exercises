#Ler uma temperatura em graus Celsius e apresenta-la convertida em graus Fahrenheit. 
#A fórmula de conversão é: F=(9*C+160)/%, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.


C=float(input("Digite a temperatura em graus celsius para converter em Fahrenheit:"))
F=(9*C+160)/5
print(f"A temperatura em Fahrenheit é {F}")