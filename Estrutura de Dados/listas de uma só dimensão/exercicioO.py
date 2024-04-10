a = []  # Lista vazia para armazenar as temperaturas
b=[] # Lista vazia para armazenar as temperaturas
cont = 0  # Variável para contar os dias

# Loop para solicitar as temperaturas dos dias
for i in range(7):
    a.append(int(input(f"Digite a temperatura do {cont+1}º dia em graus Celsius: ")))
    b.append(a[i]*9/5+32)
    cont += 1

print(a)  # Exibe a temperatura em celsius
print(b)  # Exibe a temperatura em fahrenheit

amenorvalor = min(a)  # Encontra a menor temperatura em celsius
amaiorvalor = max(a)  # Encontra a maior temperatura em celsius
print("A menor temperatura em celsius foi: ", amenorvalor)  # Exibe a menor temperatura em celsius
print("A maior temperatura em celsius foi: ", amaiorvalor)  # Exibe a maior temperatura em celsius

bmenorvalor = min(b)  # Encontra a menor temperatura em fahtrenheit
bmaiorvalor = max(b)  # Encontra a maior temperatura em fahrenheit

print("A menor temperatura em celsius foi: ", bmenorvalor)  # Exibe a menor temperatura em fahtrenheit
print("A maior temperatura em celsius foi: ", bmaiorvalor)  # Exibe a maior temperatura em fahrenheit