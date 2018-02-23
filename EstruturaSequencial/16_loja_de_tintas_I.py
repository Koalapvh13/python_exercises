# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math
area = float(input('Qual o tamanho da área a ser pintada? (em m²): '))
lata_cobertura = 18*3
lata_preco = 80.0
latas = math.ceil(area/lata_cobertura)
print('Área a ser pintada: {} M²\nLatas de tinta: {} Unid.\nTotal a pagar: R$ {:.2f}'.format(area, latas, (latas*lata_preco)))
