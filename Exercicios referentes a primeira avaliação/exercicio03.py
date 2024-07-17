'''
Escreva um progama que calcule o imposto de renda a parTr de um salário de
um funcionário a parTr de da tabela abaixo:
Sálario IPRF
Ate 1.500,00 5%
Acima de 1500,00 até 3.000,00 8%
Acima de 3.000,00 até 10.000,00 15%
Acima de 15.000,00 27%
O programa deverá ao fim imprimir o valor deo imposto devido, o saláriio bruto
e o salário com desconto. O programa ainda deverá se repeTr até que o
usuário deseje encerra-lo.'''

ysalario= int(input("Digite o salário do funcionário: "))
while ysalario > 0:
    if ysalario <= 1500:
        imposto = ysalario * 0.05
    elif ysalario <= 3000:
        imposto = ysalario * 0.08
    elif ysalario <= 10000:
        imposto = ysalario * 0.15
    else:
        imposto = ysalario * 0.27
    print(f"Salário bruto: {ysalario}")
    print(f"Imposto devido: {imposto}")
    print(f"Salário com desconto: {ysalario - imposto}")
    ysalario= int(input("Digite o salário do funcionário: "))