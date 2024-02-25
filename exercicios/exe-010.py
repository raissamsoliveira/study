#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
din = float(input('Quanto você tem na sua carteira? R$ '))
dol = din/5.37
print('Com R${} você pode comprar US${:.2f}.'.format(din,dol))