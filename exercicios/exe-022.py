'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúculas e minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome 
'''

nome = str(input('Digite seu nome completo: ')).strip()                  #já elimina os espaços antes e depois do nome
print ('O seu nome com letras maiúsculas é {}'.format(nome.upper()))
print ('O seu nome com letras minúsculas é {}'.format(nome.lower()))
print ('O seu nome possui {} letras.'.format(len(nome)-nome.count(' ')))    #nome.count - contador de espaços             
print ('O seu primeiro nome tem {} letras. '.format(nome.find(' ')))

lista = nome.split()
print ('O seu primeiro nome é {} e possui {} letras.'.format(lista[0], len(lista [0])))
