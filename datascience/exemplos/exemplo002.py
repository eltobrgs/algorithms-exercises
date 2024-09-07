import pandas as pd

# Cria um dicionario que posteriormente será convertido em um DataFrame
data= {'nome':['João', 'Maria', 'José', 'Ana'],
       'ídade':[16,17,18,19],
        'sexo':['M','F','M','F'],
        'genero':['Masculino','Feminino','Masculino','Feminino'],
        'sexualidade':['Heterossexual','Homossexual','Bissexual','Heterossexual'],
        'cidade':['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo']
        }

# Converte o dicionario em um DataFrame
df= pd.DataFrame(data)

# Exibe o DataFrame
print(df)

# Exibe a média das idades
print("")
print("Média das idades das pessoas é:", df['ídade'].mean())

# Exibe a moda das sexualidade das pessoas
print("")
print("A sexualidade com mais incidencia entre as pessoas é:", df['sexualidade'].mode())

# Exibe a moda das genero das pessoas
print("")
print("o genero com mais incidencia entre as pessoas é:", df['genero'].mode())

# exibe a cidade com mais incidencia
print("")
print("A cidade com mais incidencia entre as pessoas é:", df['cidade'].mode())