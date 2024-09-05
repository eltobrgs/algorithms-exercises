# importando nossas funcoes do arquivo functionsofsystem.py
import functionsofsystem

#Dicionario para armazenar os seguintes dados
lista_medicos = [] # lista medicos
lista_pacientes = [] # lista pacientes
lista_consultas = [] # lista consultas

def main():
    while True:  
        try:
            print("\n=== Sistema de Controle de Consultas ===")
            print("1 - Cadastrar médico")#funcionalidade implementada
            print("2 - Excluir médico") #funcionalidade ainda nao implementada
            print("3 - Listar médicos")#funcionalidade implementada

            print("4 - Cadastrar paciente")#funcionalidade implementada
            print("5 - Excluir paciente") #funcionalidade ainda nao implementada
            print("6 - Listar pacientes")#funcionalidade implementada

            print("7 - Agendar consulta")#funcionalidade implementada
            print("8 - Excluir consulta") #funcionalidade ainda nao implementada
            print("9 - Listar consultas") #funcionalidade implementada

            print("0 - Sair do sistema")

            opcao = input("Digite a opção: ")
            if opcao == "1":
                functionsofsystem.cadastrar_medico()
            elif opcao == "2":
                functionsofsystem.excluir_medico()
            elif opcao == "3":
                functionsofsystem.listar_medicos()
            elif opcao == "4":
                functionsofsystem.cadastrar_paciente()
            elif opcao == "5":
                functionsofsystem.excluir_paciente()
            elif opcao == "6":
                functionsofsystem.listar_pacientes()
            elif opcao == "7":
                functionsofsystem.agendar_consulta()
            elif opcao == "8":
                functionsofsystem.excluir_consulta()
            elif opcao == "9":
                functionsofsystem.listar_consultas()
            elif opcao == "0":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, digite uma opção válida.")
        except Exception as e:
            print("Ocorreu um erro:", str(e))
            break
            #mostra o erro que ocorreu no sistema e quenra a execucao do programa


if __name__ == "__main__":
    main()
