#Elaborar um programa que efetue o calculo do reajuste de salário de
#um funcionário. Considerando que o funcionário deverá receber um
#reajuste de 15% caso seu salário seja menor que 500. Se o salário for
#maior ou igual a 500, mas menor ou igual a 1000, seu reajuste será de
#10%; caso seja maior que 1000, o reajuste deverá ser de 5%.

salario= float(input('qual é o seu atual salario?'))

if salario<500:
    salario+=(15/100)*salario
elif salario>=500 and salario<=1000:
    salario+=(10/100)*salario
else:
    salario+=(5/100)*salario
print(salario)


