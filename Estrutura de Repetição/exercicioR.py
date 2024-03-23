
maior = float('-inf')  # Inicializa o maior número com o menor valor possível
menor = float('inf')   # Inicializa o menor número com o maior valor possível

n = 0
while n >= 0:
    n = int(input("Digite um valor: "))
    if n >= 0:
        maior = max(maior, n)
        menor = min(menor, n)

print("O maior número é:", maior)
print("O menor número é:", menor)
