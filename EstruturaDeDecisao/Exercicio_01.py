# Faça um programa que peça dois números e imprima o maior deles

import os

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))

if n1>n2:
    print('O maior número é ', n1)
else:
    print('O maior número é ', n2)

os.system('pause')
