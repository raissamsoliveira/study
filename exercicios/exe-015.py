'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado. 
'''
d = int(input('Dias de aluguel do carro: '))
km = float (input('Quantidade de KM percorrido: '))
valor = (d*60) + (km*0.15)

print ('O carro ficou alugado por {} dias, e foram percorridos {:.0f}Km. Com isso, a quantidade a se pagar pelo aluguel do carro é de R${:.2f}'.format(d,km, valor))