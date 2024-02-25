#Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros
x = float(input('Digite um valor: '))
xc = x*100
xm = x*1000
print ('A medida de {}m possui {} centímetros e {} milímetros.'.format(x,xc,xm))
#ou
print ('{}m = {:.0f}cm'.format(x,xc))
print ('{}m = {:.0f}dm'.format(x,xm))
