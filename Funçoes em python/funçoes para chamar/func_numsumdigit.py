
# Função para calcular a soma dos dígitos de um número
def sum_of_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

