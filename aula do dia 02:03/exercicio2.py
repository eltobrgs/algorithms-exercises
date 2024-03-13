n1 = float(input("digite o valor da primeira nota:"))
n2 = float(input("digite o valor da segunda nota:"))
n3 = float(input("digite o valor da terceira nota:"))
n4 = float(input("digite o valor da quarta nota:"))
nf = (n1 + n2 + n3 + n4) / 4
if nf >= 7:
    print("Aprovado")
else:
    print("suas notas nao foram bastantes.")
    nn = float(input("digite a nota do exame final:"))
    if (nf + nn) / 2 >= 5:
        print("Aprovado em exame final")
    else:
        print("Reprovado")
