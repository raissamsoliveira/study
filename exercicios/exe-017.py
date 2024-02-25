'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
#hip = math.sqrt((co**2)+(ca**2)) #forma tradicional
hip = math.hypot(co, ca)
print ('A hipotenusa do triângulo é {:.2f}.'.format(hip))