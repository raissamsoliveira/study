'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome deparadamente.
'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print ('Analisando seu nome completo.. {}'.format(n))
print ('Primeiro nome: {}.'.format(nome[0]))
print ('Segundo nome: {}.'.format(nome[len(nome) - 1]))
