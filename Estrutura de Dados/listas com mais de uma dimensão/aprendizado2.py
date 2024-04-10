temps=[[0.0 for h in range(24)] for d in range(31)]
#the matrix is is magically update here
print (temps)
sum=0.0
for day in temps:
    sum+=day[11]
average=sum/31
print("Average temperature at noon:",average)


