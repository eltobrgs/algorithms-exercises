
prova_I = float(input("Informe a nota do exame I: "))
prova_II = float(input("Informe a nota do exame II: "))
prova_III = float(input("Informe a nota do exame III: "))
prova_IV = float(input("Informe a nota do exame IV: "))
prova_V = float(input("Informe a nota do exame V: "))


media = (prova_I + prova_II + prova_III + prova_IV + prova_V) / 5


if media >= 7.0:
    print("Classificação: A - passou em todos os exames")
elif prova_I >= 7.0 and prova_II >= 7.0 and prova_IV >= 7.0 and (prova_III < 7.0 or prova_V < 7.0):
    print("Classificação: B - passou em I, II e IV, mas não em III ou V")
elif prova_I >= 7.0 and prova_II >= 7.0 and (prova_III >= 7.0 or prova_IV >= 7.0) and prova_V < 7.0:
    print("Classificação: C - passou em I e II, III ou IV, mas não em V")
else:
    print("Classificação: Reprovado")