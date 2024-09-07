import Funcs

def main(): #função principal que chama as outras funções do sistema, é a função que inicia o sistema e a que controla o fluxo do sistema, a fução main é a função principal de um programa e geralmente a que é chamada para iniciar a execução do programa
    while True:
        try:
            Funcs.menu()
            option = input('Digite a opção desejada: ')

            if option == '1': #se a opção for 1, chama a função de catalogar serviço
                Funcs.catalogar_serv()
            elif option == '2': #se a opção for 2, chama a função de listar serviços
                Funcs.listar_serv()
            elif option == '3':
                Funcs.cadastrar_pet() #... e assim por diante
            elif option == '4':
                Funcs.listar_pets()
            elif option == '5':
                Funcs.agendar_servico()
            elif option == '6':
                Funcs.listar_agendamentos()
            elif option == '7':
                Funcs.cancelar_servico()
            elif option == '0':
                print('Saindo do sistema...')
                break
        except Exception as e:
            print('Ocorreu um erro:', str(e))
            break


    
if __name__ == "__main__": #se o arquivo for executado diretamente, chama a função main
    main()
