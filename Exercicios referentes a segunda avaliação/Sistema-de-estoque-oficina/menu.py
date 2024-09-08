import funcs

def main():
    while True:
        try:
            funcs.menu()
            if funcs.menu() == "1":
                funcs.cadastrar_peça()
            elif funcs.menu() == "2":
                funcs.listar_peças()
            elif funcs.menu() == "3":
                funcs.vender_peça()
            elif funcs.menu() == "4":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
                return

        except ValueError:
            print("Digite um número inteiro.")
            continue


if __name__ =='__main__':
    main()