a=[]
b=[]
c=[]
for i in range(5):
    a.append(int(input(f"Digite {i+1} número inteiro: ")))
    b.append(int(input(f"Digite {i+1} número inteiro: ")))
    c.append(a[i]-b[i])
print (a)
print (b)
print (c)
