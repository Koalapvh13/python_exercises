#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#I - o produto do dobro do primeiro com metade do segundo .
#II - a soma do triplo do primeiro com o terceiro.
#III - o terceiro elevado ao cubo.
import os
int1 = int(input('Informe um número inteiro: '))
int2 = int(input('Informe outro número inteiro: '))
real = float(input('Informe um número real: '))
primeira_operacao = (2*int1) * (int2/2)
segunda_operacao = (3*int1) + real
terceira_operacao = real**3
print('=> (2*{})*({}/2) = {};\n'
      '=> 3*{}+{:.2f} = {};\n'
      '=> ({})³ = {}.'
      .format(int1, int2, primeira_operacao, int1, real, segunda_operacao, real, terceira_operacao))
os.system('pause')