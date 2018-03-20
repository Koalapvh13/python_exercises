#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math,os

raio = float(input('Informe o raio: '))
area = math.pi*(raio**2)

print('O círculo de raio {}, tem área de {:.1f} \n'.format(raio, area))
print('''     A = π*r²
     A = 3.14*({:.0f})²
     A = {:.1f}'''.format(raio, area))
os.system('pause')