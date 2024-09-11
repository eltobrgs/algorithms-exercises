# importando nossas funções do arquivo functionsofsystem.py
import functionsofsystem

def main(): 
    while True: # Loop infinito
        try:
            print("\n=== Sistema de Controle de Consultas ===")
            print("1 - Cadastrar médico")
            print("2 - Excluir médico")
            print("3 - Listar médicos")
            print("4 - Pesquisar médico")

            print("5 - Cadastrar paciente")
            print("6 - Excluir paciente")
            print("7 - Listar pacientes")
            print("8 - Pesquisar paciente")

            print("9 - Agendar consulta")
            print("10 - Excluir consulta")
            print("11 - Listar consultas")
            print("12 - Pesquisar consulta")

            print("0 - Sair do sistema")

            opcao = input("Digite a opção: ")

            if opcao == "1":
                functionsofsystem.cadastrar_medico()
            elif opcao == "2":
                functionsofsystem.excluir_medico()
            elif opcao == "3":
                functionsofsystem.listar_medicos()
            elif opcao == "4":
                functionsofsystem.pesquisar_medico()  # Corrigido
            elif opcao == "5":
                functionsofsystem.cadastrar_paciente()
            elif opcao == "6":
                functionsofsystem.excluir_paciente()
            elif opcao == "7":
                functionsofsystem.listar_pacientes()
            elif opcao == "8":
                functionsofsystem.pesquisar_paciente()  # Corrigido
            elif opcao == "9":
                functionsofsystem.agendar_consulta()
            elif opcao == "10":
                functionsofsystem.excluir_consulta()
            elif opcao == "11":
                functionsofsystem.listar_consultas()
            elif opcao == "12":
                functionsofsystem.pesquisar_consulta()  # Corrigido
            elif opcao == "0":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, digite uma opção válida.")
        except Exception as e:
            print("Ocorreu um erro:", str(e))
            break


if __name__ == "__main__":
    main()
