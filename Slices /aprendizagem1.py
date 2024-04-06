a= [5, 3, 8, 1, 9, 2, 7, 4, 6, 10, 14, 11, 13, 12, 15]
print('Sem ordenaçao:', a)

for i in range (len(a)-1):
    for j in range (1+i, len(a)):
        if a[i]>a[j]:
            a[i], a[j]= a[j], a[i] 

print('Ordernado com bubble sort:', a)

print('Ordenado em ordem de-crescente com slice', a[::-1])