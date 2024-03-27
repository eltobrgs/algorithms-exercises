a = []  # Lista vazia para armazenar as temperaturas
cont = 0  # Variável para contar os dias

# Loop para solicitar as temperaturas dos dias
for i in range(7):
    a.append(int(input(f"Digite a temperatura do {cont+1}º dia em graus Celsius: ")))
    menorvalor = min(a)  # Encontra a menor temperatura atualizada
    maiorvalor = max(a)  # Encontra a maior temperatura atualizada

print("A menor temperatura foi: ", menorvalor)  # Exibe a menor temperatura
print("A maior temperatura foi: ", maiorvalor)  # Exibe a maior temperatura