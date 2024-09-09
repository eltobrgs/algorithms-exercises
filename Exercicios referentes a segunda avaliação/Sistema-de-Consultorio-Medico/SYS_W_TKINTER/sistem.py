import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from time import sleep

# Listas
lista_medicos = []
lista_pacientes = []
lista_consultas = []

def cpf_valido(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    else:
        cpf = [int(digit) for digit in cpf]
        soma1 = 0
        for i in range(9):
            soma1 += cpf[i] * (10 - i)
        digito1 = (soma1 * 10 % 11) % 10

        soma2 = 0
        for i in range(10):
            soma2 += cpf[i] * (11 - i)
        digito2 = (soma2 * 10 % 11) % 10

        return digito1 == cpf[9] and digito2 == cpf[10]

def cadastrar_medico():
    nome = simpledialog.askstring("Cadastrar Médico", "Digite o nome do médico:")
    especialidade = simpledialog.askstring("Cadastrar Médico", "Digite a especialidade:")
    credencial = simpledialog.askstring("Cadastrar Médico", "Digite a credencial do médico:")
    limite = simpledialog.askinteger("Cadastrar Médico", "Digite o limite de atendimentos por dia (máximo 5):", minvalue=1, maxvalue=5)

    for medico in lista_medicos:
        if medico['credencial'] == credencial:
            messagebox.showerror("Erro", "Médico já cadastrado!")
            return

    medico = {'nome': nome, 'especialidade': especialidade, 'credencial': credencial, 'limite': limite}
    lista_medicos.append(medico)
    messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")

def listar_medicos():
    if not lista_medicos:
        messagebox.showinfo("Lista de Médicos", "Nenhum médico cadastrado!")
    else:
        medicos = ""
        for i, medico in enumerate(lista_medicos):
            medicos += f"{i + 1}. {medico['nome']} - {medico['especialidade']}\n"
        messagebox.showinfo("Lista de Médicos", medicos)

def excluir_medico():
    listar_medicos()
    indice = simpledialog.askinteger("Excluir Médico", "Digite o índice do médico para excluir:")
    if 0 < indice <= len(lista_medicos):
        lista_medicos.pop(indice - 1)
        messagebox.showinfo("Sucesso", "Médico excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Índice inválido!")

def cadastrar_paciente():
    nome = simpledialog.askstring("Cadastrar Paciente", "Digite o nome do paciente:")
    cpf = simpledialog.askstring("Cadastrar Paciente", "Digite o CPF do paciente (somente números):")

    if not cpf_valido(cpf):
        messagebox.showerror("Erro", "CPF inválido!")
        return

    for paciente in lista_pacientes:
        if paciente['cpf'] == cpf:
            messagebox.showerror("Erro", "Paciente já cadastrado!")
            return

    email = simpledialog.askstring("Cadastrar Paciente", "Digite o e-mail do paciente:")
    paciente = {'nome': nome, 'cpf': cpf, 'email': email}
    lista_pacientes.append(paciente)
    messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")

def listar_pacientes():
    if not lista_pacientes:
        messagebox.showinfo("Lista de Pacientes", "Nenhum paciente cadastrado!")
    else:
        pacientes = ""
        for i, paciente in enumerate(lista_pacientes):
            pacientes += f"{i + 1}. {paciente['nome']} - CPF: {paciente['cpf']}, Email: {paciente['email']}\n"
        messagebox.showinfo("Lista de Pacientes", pacientes)

def excluir_paciente():
    listar_pacientes()
    indice = simpledialog.askinteger("Excluir Paciente", "Digite o índice do paciente para excluir:")
    if 0 < indice <= len(lista_pacientes):
        lista_pacientes.pop(indice - 1)
        messagebox.showinfo("Sucesso", "Paciente excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Índice inválido!")

def verificar_limite_consultas(medico_escolhido, dia_consulta):
    consultas_do_dia = [consulta for consulta in lista_consultas if consulta['medico_escolhido'] == medico_escolhido and consulta['dia_consulta'] == dia_consulta]
    medico = next((med for med in lista_medicos if med['nome'] == medico_escolhido), None)
    if medico and len(consultas_do_dia) < medico['limite']:
        return True
    else:
        messagebox.showinfo("Limite de Consultas", "Médico atingiu o máximo de consultas!")
        return False

def agendar_consulta():
    nome_paciente = simpledialog.askstring("Agendar Consulta", "Digite o nome do paciente:")
    cpf_paciente = simpledialog.askstring("Agendar Consulta", "Digite o CPF do paciente (somente números):")

    paciente = next((pac for pac in lista_pacientes if pac['cpf'] == cpf_paciente and pac['nome'] == nome_paciente), None)
    if not paciente:
        messagebox.showinfo("Paciente não cadastrado", "Paciente não encontrado. Cadastrando novo paciente.")
        cadastrar_paciente()

    listar_medicos()
    medico_escolhido = simpledialog.askstring("Agendar Consulta", "Com que médico deseja se consultar?")
    medico = next((med for med in lista_medicos if med['nome'] == medico_escolhido), None)
    if not medico:
        messagebox.showerror("Erro", "Médico não encontrado!")
        return

    dia_consulta = simpledialog.askstring("Agendar Consulta", "Qual o dia da consulta?")

    if not verificar_limite_consultas(medico_escolhido, dia_consulta):
        return

    hora_consulta = simpledialog.askstring("Agendar Consulta", "Qual o horário da consulta?")
    consulta = {'nome_paciente': nome_paciente, 'cpf_paciente': cpf_paciente, 'medico_escolhido': medico_escolhido, 'dia_consulta': dia_consulta, 'hora_consulta': hora_consulta}
    lista_consultas.append(consulta)
    messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")

def listar_consultas():
    if not lista_consultas:
        messagebox.showinfo("Lista de Consultas", "Nenhuma consulta agendada!")
    else:
        consultas = ""
        for i, consulta in enumerate(lista_consultas):
            consultas += f"{i + 1}. Paciente: {consulta['nome_paciente']}, Médico: {consulta['medico_escolhido']}, Dia: {consulta['dia_consulta']}, Hora: {consulta['hora_consulta']}\n"
        messagebox.showinfo("Lista de Consultas", consultas)

def excluir_consulta():
    listar_consultas()
    indice = simpledialog.askinteger("Excluir Consulta", "Digite o índice da consulta para excluir:")
    if 0 < indice <= len(lista_consultas):
        lista_consultas.pop(indice - 1)
        messagebox.showinfo("Sucesso", "Consulta excluída com sucesso!")
    else:
        messagebox.showerror("Erro", "Índice inválido!")

def pesquisar_medico():
    nome_medico = simpledialog.askstring("Pesquisar Médico", "Digite o nome do médico que deseja pesquisar:")
    medico = next((med for med in lista_medicos if med['nome'] == nome_medico), None)
    if medico:
        messagebox.showinfo("Médico Encontrado", f"Médico: {medico['nome']}\nEspecialidade: {medico['especialidade']}\nCredencial: {medico['credencial']}\nLimite de atendimentos: {medico['limite']}")
        resposta = simpledialog.askstring("Agendar Consulta", "Deseja se consultar com esse médico? (S/N)").upper()
        if resposta == "S":
            agendar_consulta()
        else:
            messagebox.showinfo("Encerramento", "Obrigado... Tchau!")
    else:
        messagebox.showerror("Erro", "Médico não encontrado!")

def pesquisar_paciente():
    nome_paciente = simpledialog.askstring("Pesquisar Paciente", "Digite o nome do paciente que deseja pesquisar:")
    paciente = next((pac for pac in lista_pacientes if pac['nome'] == nome_paciente), None)
    if paciente:
        messagebox.showinfo("Paciente Encontrado", f"Paciente: {paciente['nome']}\nCPF: {paciente['cpf']}\nEmail: {paciente['email']}")
        resposta = simpledialog.askstring("Agendar Consulta", "Deseja agendar uma consulta para esse paciente? (S/N)").upper()
        if resposta == "S":
            agendar_consulta()
        else:
            messagebox.showinfo("Encerramento", "Obrigado... Tchau!")
    else:
        messagebox.showerror("Erro", "Paciente não encontrado!")

def pesquisar_consulta():
    cpf_paciente = simpledialog.askstring("Pesquisar Consulta", "Digite o CPF do paciente que deseja pesquisar a consulta:")
    consultas_paciente = [cons for cons in lista_consultas if cons['cpf_paciente'] == cpf_paciente]
    if consultas_paciente:
        consultas = ""
        for i, consulta in enumerate(consultas_paciente):
            consultas += f"{i + 1}. Médico: {consulta['medico_escolhido']}, Dia: {consulta['dia_consulta']}, Hora: {consulta['hora_consulta']}\n"
        messagebox.showinfo("Consultas Encontradas", consultas)
    else:
        messagebox.showerror("Erro", "Nenhuma consulta encontrada para o CPF informado!")

def criar_interface():
    root = tk.Tk()
    root.title("Sistema de Consultório")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="Cadastrar Médico", command=cadastrar_medico).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame, text="Listar Médicos", command=listar_medicos).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame, text="Excluir Médico", command=excluir_medico).grid(row=0, column=2, padx=5, pady=5)

    tk.Button(frame, text="Cadastrar Paciente", command=cadastrar_paciente).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame, text="Listar Pacientes", command=listar_pacientes).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(frame, text="Excluir Paciente", command=excluir_paciente).grid(row=1, column=2, padx=5, pady=5)

    tk.Button(frame, text="Agendar Consulta", command=agendar_consulta).grid(row=2, column=0, padx=5, pady=5)
    tk.Button(frame, text="Listar Consultas", command=listar_consultas).grid(row=2, column=1, padx=5, pady=5)
    tk.Button(frame, text="Excluir Consulta", command=excluir_consulta).grid(row=2, column=2, padx=5, pady=5)

    tk.Button(frame, text="Pesquisar Médico", command=pesquisar_medico).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(frame, text="Pesquisar Paciente", command=pesquisar_paciente).grid(row=3, column=1, padx=5, pady=5)
    tk.Button(frame, text="Pesquisar Consulta", command=pesquisar_consulta).grid(row=3, column=2, padx=5, pady=5)

    root.mainloop()

criar_interface()
