import funcoes

def main():
    while True:
        try:
            print("1 - Cadastrar evento")
            print("2 - Listar eventos")
            print("3 - Cadastrar participante")
            print("4 - Listar participantes")
            print("5 - Excluir participante")
            print("6 - Excluir evento")
            print("0 - Sair do sistema")
            
            op = int(input("Digite a opção desejada: "))
            
            if op == 1:
                funcoes.cadastrar_evento()
            elif op == 2:
                funcoes.listar_eventos()
            elif op == 3:
                funcoes.cadastrar_participante()
            elif op == 4:
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
        except ValueError:
            print("Digite um valor válido!")

if __name__ == "__main__":
    main()