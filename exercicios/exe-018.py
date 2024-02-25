''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ânuglo.'''

import math
a = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print ('O seno do ângulo {}º é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(a,sen,cos,tg))