import funcoes

def main():
    while True:
        try:
            print('1 - Cadastrar cliente')
            print('2 - Listar clientes')
            print('3 - Excluir cliente')
            print('4 - Cadastrar carro')
            print('5 - Listar carros')
            print('6 - Gerar relatório de serviço prestado')
            print('0 - Sair do sistema')

            op = int(input('Digite a opção desejada: '))    

            if op == 1:
                funcoes.cadastrar_cliente()    
            elif op == 2:
                funcoes.listar_clientes()
            elif op == 3:
                funcoes.excluir_cliente()
            elif op == 4:
                funcoes.cadastrar_carro()
            elif op == 5:
                funcoes.listar_carros()
            elif op == 6:
                funcoes.relatorio()
            elif op == 0:
                print('Saindo do sistema de oficina... TCHAU!')
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Digite um valor válido!')

if __name__ == '__main__':
    main()
