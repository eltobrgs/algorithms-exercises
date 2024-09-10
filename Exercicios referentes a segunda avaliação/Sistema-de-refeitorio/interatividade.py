import modulos

def main():
    while True:
        try:
            print('1 - Cadastrar aluno')
            print('2 - Listar alunos')
            print('3 - Listar alunos por refeição')
            print('4 - pesquisar aluno')
            print('5 - Excluir aluno')
            print('6 - Sair')

            op = int(input('Digite a opção desejada: '))    

            if op == 1:
                modulos.cadastrar_aluno()    
            elif op == 2:
                modulos.listar_alunos()
            elif op == 3:
                modulos.listar_alunos_por_refeicao()
            elif op == 4:
                modulos.pesquisar_aluno()
            elif op == 5:
                modulos.excluir_aluno()
            elif op == 6:
                print('Saindo do sistema de refeitório... TCHAU!')
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Digite um valor válido!')

if __name__ == '__main__':
    main()
