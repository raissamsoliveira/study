nome = input('Qual é o seu nome? ')

#testando espaços
print ('Prazer em te conhecer, {}!'.format(nome))
print ('Prazer em te conhecer, {:20}!'.format(nome))
print ('Prazer em te conhecer, {:>20}!'.format(nome))
print ('Prazer em te conhecer, {:<20}!'.format(nome))
print ('Prazer em te conhecer, {:^20}!'.format(nome))
print ('Prazer em te conhecer, {:=^20}!'.format(nome))

#Operadores Aritméticos

a = int(input("Digite o primeiro valor: "))
b = int(input('Digite o segundo valor: '))
print ('A soma vale: {}'.format(a+b))
print ('A multiplicação vale: {}.'.format(a*b))
print ('A divisão vale: {:.3f}.'.format (a/b))       #limitando a divisão em 3 casas decimais
s = a + b
m = a*b
d = a/b
d1 = a//b
r = a%b
print ('A soma é {}, a multiplicação é {} e a divisão é {}. '.format(s,m,d)) 
print ('A divisão inteira é {} e o resto dessa divisão é {}.'.format(d1,r))

#Se eu quero o resultado dos dois prints na mesma linha, posso utilizar o end = ' ' após o format. E para realizar a quebra de linha, utilizo o \n
