import funcoes   #importando o arquivo funcoes.py, onde estão as funções do sistema

def main():  #função principal do sistema. Aqui é onde o usuário interage com o sistema
    while True: #laço de repetição para que o menu seja exibido até que o usuário escolha sair do sistema
        try: #bloco try/except para tratar exceções

            #menu do sistema    
            print("1 - Cadastrar evento")
            print("2 - Listar eventos")
            print("3 - Cadastrar participante")
            print("4 - Listar participantes")
            print("5 - Excluir participante")
            print("6 - Excluir evento")
            print("7 - procurar participante")
            print("8 - procurar evento")
            print("0 - Sair do sistema")
            
            #opção escolhida pelo usuário
            op = int(input("Digite a opção desejada: "))
            
            if op == 1: #se a opção escolhida for 1, chama a função cadastrar_evento do arquivo funcoes.py
                funcoes.cadastrar_evento()
            elif op == 2: #se a opção escolhida for 2, chama a função listar_eventos do arquivo funcoes.py
                funcoes.listar_eventos()
            elif op == 3: #se a opção escolhida for 3, chama a função cadastrar_participante do arquivo funcoes.py
                funcoes.cadastrar_participante()
            elif op == 4: #... e assim por diante
                funcoes.listar_participantes()
            elif op == 5:
                funcoes.excluir_participante()
            elif op == 6:
                funcoes.excluir_evento()
            elif op== 7:
                funcoes.listar_participante()
            elif op== 8:
                funcoes.listar_evento()
            elif op == 0:
                print("Saindo do sistema...")
                break 
            else:
                print("Opção inválida!")
        except ValueError: #tratamento de exceção para caso o usuário digite um valor inválido
            print("Digite um valor válido!")

if __name__ == "__main__":
    main()