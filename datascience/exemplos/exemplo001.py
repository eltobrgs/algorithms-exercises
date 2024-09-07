import pandas as pd

# Cria um DataFrame
df = pd.DataFrame({
    'Nome': ['João', 'Maria', 'José', 'Ana'],
    'Idade': [25, 30, 35, 40],
    'Sexo': ['M', 'F', 'M', 'F'],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
})

# Exibe o DataFrame
print(df)

# Exibe a média das idades
print("")
print("Media das idades das pessoas é:", df['Idade'].mean())




