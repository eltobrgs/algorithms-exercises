import numpy as np

# Criando um array de 1 dimensão
a = np.array([1, 2, 3, 4, 5])
print(a)

# Criando um array de 2 dimensões
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# operaçoes com arrays 
# Soma
print(a + 2)
# Subtração
print(a - 2)
# Multiplicação
print(a * 2)
# Divisão
print(a / 2)
# Exponenciação
print(a ** 2)
# Seno
print(np.sin(a))
# Cosseno
print(np.cos(a))
# Tangente
print(np.tan(a))
# Logaritmo natural
print(np.log(a))
# Exponencial
print(np.exp(a))
# somar arrays
print(a + a)
# subtrair arrays
print(a - a)
# media dos numeros de um array
print(a.mean())
# soma dos numeros de um array
print(a.sum())
# menor numero de um array
print(a.min())
# maior numero de um array
print(a.max())
# desvio padrão de um array
print(a.std())