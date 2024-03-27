a=[]
b=[]
for i in range(5):
    a.append(int(input("Digite um número real para lista a: ")))
a.sort()  
b.append(sum(a)) 

print(a)
print(f'a somatoria da lista a é: {b}')

