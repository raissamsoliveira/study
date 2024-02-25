'''Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tina pinta uma área de 2m2. 
'''

l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
tinta = a/2
print ('A área da parede é {:.2f}m2. São necessários {:.2f}L de tinta para pintar a parede.'.format(a,tinta))