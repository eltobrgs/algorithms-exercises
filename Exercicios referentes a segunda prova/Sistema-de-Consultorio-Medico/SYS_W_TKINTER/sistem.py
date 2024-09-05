import tkinter as tk
from tkinter import messagebox, simpledialog
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
        soma1 = sum(cpf[i] * (10 - i) for i in range(9))
        digito1 = (soma1 * 10 % 11) % 10
        soma2 = sum(cpf[i] * (11 - i) for i in range(10))
        digito2 = (soma2 * 10 % 11) % 10
        return digito1 == cpf[9] and digito2 == cpf[10]

def cadastrar_medico():
    nome = simpledialog.askstring("Cadastrar Médico", "Digite o nome do médico:")
    especialidade = simpledialog.askstring("Cadastrar Médico", "Digite a especialidade:")
    credencial = simpledialog.askstring("Cadastrar Médico", "Digite a credencial do médico:")
    limite = simpledialog.askinteger("Cadastrar Médico", "Digite o limite de atendimentos por dia:(maximo 5)")
    
    if any(medico['credencial'] == credencial for medico in lista_medicos):
        messagebox.showerror("Erro", "Médico já cadastrado!")
        return
    
    medico = {'nome': nome, 'especialidade': especialidade, 'credencial': credencial, 'limite': limite}
    lista_medicos.append(medico)
    messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")

def listar_medicos():
    if not lista_medicos:
        messagebox.showinfo("Lista de Médicos", "Nenhum médico cadastrado!")
    else:
        medicos = "\n".join([f"{i + 1}. {medico['nome']} - {medico['especialidade']}" for i, medico in enumerate(lista_medicos)])
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
    cpf = simpledialog.askstring("Cadastrar Paciente", "Digite o CPF do paciente:")
    email = simpledialog.askstring("Cadastrar Paciente", "Digite o email do paciente:")
    
    if not cpf_valido(cpf):
        messagebox.showerror("Erro", "CPF inválido!")
        return
    
    if any(paciente['cpf'] == cpf for paciente in lista_pacientes):
        messagebox.showerror("Erro", "Paciente já cadastrado!")
        return
    
    paciente = {'nome': nome, 'cpf': cpf, 'email': email}
    lista_pacientes.append(paciente)
    messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")

def listar_pacientes():
    if not lista_pacientes:
        messagebox.showinfo("Lista de Pacientes", "Nenhum paciente cadastrado!")
    else:
        pacientes = "\n".join([f"{i + 1}. {paciente['nome']} - {paciente['cpf']}" for i, paciente in enumerate(lista_pacientes)])
        messagebox.showinfo("Lista de Pacientes", pacientes)

def excluir_paciente():
    listar_pacientes()
    indice = simpledialog.askinteger("Excluir Paciente", "Digite o índice do paciente para excluir:")
    if 0 < indice <= len(lista_pacientes):
        lista_pacientes.pop(indice - 1)
        messagebox.showinfo("Sucesso", "Paciente excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Índice inválido!")

def agendar_consulta():
    listar_pacientes()
    paciente_indice = simpledialog.askinteger("Agendar Consulta", "Digite o índice do paciente:")
    
    if 0 < paciente_indice <= len(lista_pacientes):
        paciente = lista_pacientes[paciente_indice - 1]
    else:
        messagebox.showerror("Erro", "Paciente não encontrado!")
        return
    
    listar_medicos()
    medico_indice = simpledialog.askinteger("Agendar Consulta", "Digite o índice do médico:")
    
    if 0 < medico_indice <= len(lista_medicos):
        medico = lista_medicos[medico_indice - 1]
    else:
        messagebox.showerror("Erro", "Médico não encontrado!")
        return
    
    dia = simpledialog.askstring("Agendar Consulta", "Digite o dia da consulta:")
    hora = simpledialog.askstring("Agendar Consulta", "Digite a hora da consulta:")
    
    if len([c for c in lista_consultas if c['medico'] == medico['nome'] and c['dia'] == dia]) < medico['limite']:
        consulta = {'paciente': paciente['nome'], 'medico': medico['nome'], 'dia': dia, 'hora': hora}
        lista_consultas.append(consulta)
        messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
    else:
        messagebox.showerror("Erro", "Limite de consultas atingido para este médico!")

def listar_consultas():
    if not lista_consultas:
        messagebox.showinfo("Lista de Consultas", "Nenhuma consulta agendada!")
    else:
        consultas = "\n".join([f"{i + 1}. Paciente: {consulta['paciente']}, Médico: {consulta['medico']}, Dia: {consulta['dia']}, Hora: {consulta['hora']}" for i, consulta in enumerate(lista_consultas)])
        messagebox.showinfo("Lista de Consultas", consultas)

def excluir_consulta():
    listar_consultas()
    indice = simpledialog.askinteger("Excluir Consulta", "Digite o índice da consulta para excluir:")
    if 0 < indice <= len(lista_consultas):
        lista_consultas.pop(indice - 1)
        messagebox.showinfo("Sucesso", "Consulta excluída com sucesso!")
    else:
        messagebox.showerror("Erro", "Índice inválido!")

# Interface gráfica
root = tk.Tk()
root.title("Consultório Médico")

# Criação dos botões
btn_cadastrar_medico = tk.Button(root, text="Cadastrar Médico", command=cadastrar_medico)
btn_listar_medico = tk.Button(root, text="Listar Médicos", command=listar_medicos)
btn_excluir_medico = tk.Button(root, text="Excluir Médico", command=excluir_medico)

btn_cadastrar_paciente = tk.Button(root, text="Cadastrar Paciente", command=cadastrar_paciente)
btn_listar_pacientes = tk.Button(root, text="Listar Pacientes", command=listar_pacientes)
btn_excluir_paciente = tk.Button(root, text="Excluir Paciente", command=excluir_paciente)

btn_agendar_consulta = tk.Button(root, text="Agendar Consulta", command=agendar_consulta)
btn_listar_consultas = tk.Button(root, text="Listar Consultas", command=listar_consultas)
btn_excluir_consulta = tk.Button(root, text="Excluir Consulta", command=excluir_consulta)

# Layout dos botões
btn_cadastrar_medico.grid(row=0, column=0, padx=10, pady=10)
btn_listar_medico.grid(row=0, column=1, padx=10, pady=10)
btn_excluir_medico.grid(row=0, column=2, padx=10, pady=10)

btn_cadastrar_paciente.grid(row=1, column=0, padx=10, pady=10)
btn_listar_pacientes.grid(row=1, column=1, padx=10, pady=10)
btn_excluir_paciente.grid(row=1, column=2, padx=10, pady=10)

btn_agendar_consulta.grid(row=2, column=0, padx=10, pady=10)
btn_listar_consultas.grid(row=2, column=1, padx=10, pady=10)
btn_excluir_consulta.grid(row=2, column=2, padx=10, pady=10)

# Executando a interface
root.mainloop()
