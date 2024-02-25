#Faça um programa que leia um número que mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
print ("Analisando o número {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.3f}.".format(n, (n*2), (n*3), (n**(1/2))))