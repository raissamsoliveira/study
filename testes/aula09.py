'''   MANIPULANDO TEXTO  

Uma String, em seus micro-elementos, é imutável. 
Caso eu queria alterar uma palavra ou letra em uma string, preciso fazer da seguinte forma: 
frase = ' Curso em vídeo' 
frase = frase.replace ('Curso', 'Teste')

'''

#Fatiamento
frase = "Curso em Vídeo Python"
print (frase)
print (frase[9])
print (frase[9:13])         #comece no item 9, vai até o 13, mas exclui o 13.
print (frase[9:21:2])       #começa do 9, vai até o 20, mas pulando de 2 em 2. 
print (frase[:5])           #quando se omite o início, ele inicia do item 0.
print (frase[15:])          #quando se omite o final, ele finaliza no item 20 -que nesse caso, é incluso.
print (frase[9::3])         #inicia no 9, vai até o final, pulando de 3 em 3. 

#Análise
print (len(frase))           #comprimento do texto
print (frase.count('o'))     #quantas vezes aparecem a letra o (minúsucula)
print (frase.count('o',0,13))       #faz a contagem da letra, do espaço 0 ao espaço 13 - que não é válido
print (frase.find('deo'))           #quantas vezes encontrou o texto 'deo' e que em que momento (posição) ele inicia
print (frase.find('Android'))       #retorna o valor -1, indicando que não foi encontrada a string
print ('Curso' in frase)

#Transformação 
print (frase.replace ('Python', 'Android'))         #substitui as palavras na string, de uma forma secundária
print (frase.upper())                               #colocar toda a string em letras maiúsculas
print (frase.lower())                               #colocar toda a string em letras minúsculas
print (frase.capitalize())                          #apenas a primeira letra de toda a String fica maiúscula
print (frase.title())                               #Analisa todas as palavras, e coloca a primeira letra maiúsculo.

frase2 = '   Aprenda Python  '
print (frase2.strip ())                             #remove todos os espaços inúteis da string
print (frase2.rstrip ())                            #remove somente os espaços da direita (final da string)
print (frase2.lstrip ())                            #remove somente os espaços da esquerda (início da string)

#Divisão
print (frase.split ())              #ocorre uma divisão no local em que existem os espaços - gera uma lista com todas as palavras com uma cadeia de caracteres

#Junção
print('-'.join(frase))             #gera uma string única com o separador (-).
