a = int(input("Valor do triângulo:"))
b = int(input("Valor do triângulo:"))
c = int(input("Valor do triângulo:"))
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("Triângulo Equilatéro")
    elif a==b or a==c or c==b:
        print("Triângulo Isósceles")
    else: print("Triângulo Escaleno")
else: print("Não é um triângulo valido")