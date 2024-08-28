while True:
    try:
        num1 = int(input('Digite um número: '))  # Solicita ao usuário que digite um número
        num2 = int(input('Digite outro número: '))  # Solicita ao usuário que digite outro número
        div = num1 / num2  # Realiza a divisão

        print(f'{num1} dividido por {num2} é igual a {div}')  # Imprime o resultado da divisão
    except ZeroDivisionError:
        print('Não é possível dividir por zero')  # Trata a exceção ZeroDivisionError
    except ValueError:
        print('Digite apenas números inteiros')  # Trata a exceção ValueError
    else:
        break  # Sai do loop se nenhuma exceção for lançada
    finally:
        # Executado sempre, independentemente de ocorrer uma exceção ou não
        print("Reiniciando o programa")

print("Fim do programa")