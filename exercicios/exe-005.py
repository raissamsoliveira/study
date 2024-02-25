#Faça um programa que leia um número inteiro e mostre na tela seu antecessor e seu sucessor
n = int(input('Digite um número: '))
ant = n-1
suc = n+1
print ('O número é: {}. O seu antecessor é {}. O seu sucessor é {}.'.format(n, ant,suc))
print ('Analisando o número {}, o seu antecessor é {} e o seu sucessor é {}.'.format(n, (n-1), (n+1)))