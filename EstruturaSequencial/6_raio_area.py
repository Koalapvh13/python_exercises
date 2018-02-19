#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input('Informe o raio: '))
area = math.pi*(raio**2)

print('O círculo de raio {}, tem área de {:.1f} cm²'.format(raio, area))
