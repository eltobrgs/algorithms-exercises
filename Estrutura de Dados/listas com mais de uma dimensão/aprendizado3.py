temps=[[0.0 for h in range(24)] for d in range(31)]
print (temps)
#the matrix is is magically update here
max_temp=-100.0
for day in temps:
    for temp in day:
        if temp>max_temp:
            max_temp=temp
print("Max temperature was:",max_temp)