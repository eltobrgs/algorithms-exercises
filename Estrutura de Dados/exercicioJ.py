a=[]
b=[]
for i in range (5):
    a.append(int(input("Digite um número real para lista a: ")))
    somatorio=0
    for j in range (a[i]+1):
        somatorio*=j
    b.append(somatorio)
print(a)
print(b)