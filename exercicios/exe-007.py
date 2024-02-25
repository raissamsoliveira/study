#Desenvolva um programa que leia as duas notas de um aluno, calcula e mostre sua média. 

n1 = float(input("A primeira nota é: "))
n2 = float(input('A segunda nota é: '))
m = (n1+n2)/2
print ('As duas notas do aluno são {} e {}, e a média final é {:.2f}.'.format(n1,n2,m))


