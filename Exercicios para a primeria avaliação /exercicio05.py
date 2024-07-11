'''Escreva um programa que receba uam mensagem e a criptografe uTlizando a
cifra de césar, considerando a chave igual a 3'''

mensagem = input("Digite a mensagem a ser criptografada: ")
cripto = ""
chave = int(input("Digite a chave de criptografia: "))
for letra in mensagem:
    if letra.isalpha():
        cripto += chr((ord(letra) - 97 + chave) % 26 + 97)
    else:
        cripto += letra

print(f"A mensagem criptografada é: {cripto}")