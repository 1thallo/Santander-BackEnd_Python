"""
📅 ORGANIZADOR DE EVENTOS

📋 Descrição:
Uma empresa quer criar um organizador de eventos que divida os 
participantes em grupos de acordo com o tema escolhido.

📥 Entrada:
- Número de participantes
- Lista de participantes e o tema escolhido por cada um (nome, tema)

📤 Saída:
- Dicionário agrupando os participantes por tema
- Formato: "Tema: Participante1, Participante2"

📝 Exemplo:
Entrada:
3
Lucas, Fotografia
Ana, Viagem
Carlos, Fotografia

Saída:
Fotografia: Lucas, Carlos
Viagem: Ana
"""

# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()

    participantes, tema = linha.split(", ")

    if tema not in eventos:
        eventos[tema] = []

    eventos[tema].append(participantes)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")