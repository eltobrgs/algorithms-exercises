import functionsofconsultancy  # Importando a sua biblioteca

# Função principal do sistema
def main():
    medicos = {}
    pacientes = {}
    consultas = []

    while True:
        print("\nBem-vindo ao sistema de agendamento de consultas!")
        print("1 - Cadastrar médico")
        print("2 - Cadastrar paciente")
        print("3 - Agendar consulta")
        print("4 - Listar consultas")
        print("5 - Excluir consulta")
        print("0 - Sair do sistema")
        
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            functionsofconsultancy.cadastrar_medico(medicos)
        elif opcao == "2":
            functionsofconsultancy.cadastrar_paciente(pacientes)
        elif opcao == "3":
            functionsofconsultancy.agendar_consulta(medicos, pacientes, consultas)
        elif opcao == "4":
            functionsofconsultancy.listar_consultas(consultas)
        elif opcao == "5":
            functionsofconsultancy.excluir_consulta(consultas)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do sistema
if __name__ == "__main__":
    main()

    main()
