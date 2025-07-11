"""
SISTEMA DE ATENDIMENTO MÉDICO

Descrição:
Uma clínica médica quer automatizar seu sistema de atendimento. 
Crie uma função que organize os pacientes em ordem de prioridade 
com base na idade e na urgência do caso.

Critérios de Prioridade:
- Pacientes que apresentam "urgente" têm prioridade máxima e mais velhos
- Pacientes acima de 60 anos têm prioridade
- Os demais pacientes são atendidos por ordem de chegada

Entrada:
- Número de pacientes
- Dados: nome, idade, status

Saída:
- Lista ordenada por prioridade
"""

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def definir_prioridade(paciente):
    nome, idade, status = paciente
    
    if status == "urgente":
        return (0, -idade)
    
    elif idade >= 60:
        return (1, pacientes.index(paciente))
    
    else:
        return (2, pacientes.index(paciente))

# TODO: Exiba a ordem de atendimento com título e vírgulas:
pacientes_ordenados = sorted(pacientes, key=definir_prioridade)

nomes_ordenados = [paciente[0] for paciente in pacientes_ordenados]

print(f"Ordem de Atendimento: {', '.join(nomes_ordenados)}")