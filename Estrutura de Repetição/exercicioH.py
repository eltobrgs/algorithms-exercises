while True:
    B= int(input("Digite um número para ser a base: "))  # Solicita um número para ser a base
    E= int(input("Digite um expoente para atribuir a base: "))  # Solicita um número para ser o expoente
    resultado= B**E  # Calcula a potência da base elevada ao expoente
    if E >=0 or B >=0:
        print(f"O resultado da operação é: {resultado}")
    else: 
        print("Digite um número positivo")
        break 
        
        

'''
while True:  # Loop infinito
    for i in range(1, 4):  # Repete o loop 3 vezes
           B= int(input("Digite um número para ser a base: "))  # Solicita um número para ser a base
    E= int(input("Digite um expoente para atribuir a base: "))  # Solicita um número para ser o expoente
    resultado= B**E  # Calcula a potência da base elevada ao expoente
    if E >=0 or B >=0:
        print(f"O resultado da operação é: {resultado}")
    break 
        '''
