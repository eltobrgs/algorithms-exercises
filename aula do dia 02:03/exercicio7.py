# Ler o nome e o sexo da pessoa
nome = input("Digite o nome da pessoa: ")
sexo = input("Digite o sexo da pessoa (M para masculino ou F para feminino): ")

# Verificar o sexo e apresentar a saudação apropriada
if sexo.upper() == "M":
    print(f"Ilmo. Sr. Tenha um bom dia sr. {nome}" )
elif sexo.upper() == "F":
    print(f"Ilma. Sra. tenha um bom dia sra. {nome}")
else:
    print("Sexo não reconhecido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
