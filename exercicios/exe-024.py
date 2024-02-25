'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo". 
'''

cidade = str(input('Digite o nome da cidade que você nasceu: ')).strip()
print (cidade[0:5].upper() == 'SANTO')