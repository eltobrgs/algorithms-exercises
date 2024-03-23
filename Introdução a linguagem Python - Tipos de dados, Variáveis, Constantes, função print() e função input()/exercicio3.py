# Construir um programa que efetue o cálculo do salário líquido de um professor. Para fazer este programa você deverá possuir alguns dados, tais como: 
# o valor da hora aula, número de horas trabalhadas no mês e percentual de desconto
# do INSS. Em primeiro lugar, deve-se estabelecer qual será o seu salario para
# efetuar o desconto e ter o valor do salário liquido.

horaaula = float(input('Digite quanto recebe por hora aula:'))  # Solicita o valor da hora aula ao usuário
horatrabalhada = float(input('Digite quantas horas trabalha em um mês:'))  # Solicita o número de horas trabalhadas no mês ao usuário
descontoinss = (14/100)  # Define o percentual de desconto do INSS como 14%
salariob = horaaula * horatrabalhada  # Calcula o salário bruto multiplicando o valor da hora aula pelas horas trabalhadas
salariol = (horatrabalhada * horatrabalhada) - descontoinss  # Calcula o salário líquido subtraindo o desconto do INSS do salário bruto
print(f"O salário líquido de um professor que recebe {salariob}R$ de salário bruto é {salariol}R$")  # Imprime o resultado do cálculo do salário líquido
