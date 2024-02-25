''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random

# Lista para armazenar os nomes dos alunos
alunos = []

# Obter os nomes dos alunos
for i in range(4):
    nome_aluno = input(f"Digite o nome do aluno {i + 1}: ")
    alunos.append(nome_aluno)

# Embaralhar a ordem dos alunos
random.shuffle(alunos)

# Mostrar a ordem sorteada
print("\nOrdem de Apresentação:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")