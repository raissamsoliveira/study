#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto. 
pr = float(input('Qual o valor do produto? R$'))
desc = pr*0.05
nvpr = pr - desc
print ('O produto está no valor de R${:.f}, mas com um desconto de 5%, fica por R${:.f}.'.format(pr,nvpr))