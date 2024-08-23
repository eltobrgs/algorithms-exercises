# Exemplo de dicionário
dic = {'nome': 'Fulano', 'idade': 39}
print(dic['nome'])  # Saída: Fulano
print(dic['idade'])  # Saída: 39

dic['nome'] = 'Ciclano'  # Altera o valor associado à chave 'nome'
dic['cidade'] = 'São Paulo'  # Adiciona a chave 'cidade' ao dicionário
del dic['idade']  # Remove a entrada com a chave 'idade'

print(dic)  # Saída: {'nome': 'Ciclano', 'cidade': 'São Paulo'}

# Exemplo de conjunto
conj = {1, 2, 3}
conj.add(4)  # Adiciona o número 4 ao conjunto
conj.remove(2)  # Remove o número 2 do conjunto
print(conj)  # Saída: {1, 3, 4}








