#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo slário com 15% de aumento. 
salário = float(input('Qual o seu salário? R$'))
novo = salário + (salário*0.15)
print ('O valor do meu salário é de R${}. Com o aumento de 15%, passa a ser de R${}.'.format(salário,novo))