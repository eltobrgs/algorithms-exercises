import funcs #importando o arquivo de funçaoes 

def main():
    while True:
        try:
            print("-" * 30)
            print("Sistema de estoque da oficina:")
            print("1 - Cadastrar peça")
            print("2 - Listar peças")
            print("3 - pesquisar peça no estoque")
            print("4 - Vender peça")
            print('5- excluir peça do estoque')
            print("0 - Sair do sistema")
            print("-" * 30)

            opçao = int(input("Digite a opção desejada: "))

            if opçao == 1:
                funcs.cadastrar_peça()
            elif opçao == 2:
                funcs.listar_peças()
            elif opçao == 3:
                funcs.pesquisar_peça()
            elif opçao == 4:
                funcs.vender_peça()
            elif opçao == 5:
                funcs.excluir_peça()
            elif opçao == 0:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite um valor válido.")
            break
            

if __name__ =='__main__':
    main()