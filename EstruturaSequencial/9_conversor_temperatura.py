#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

farenheit = float(input('Farenheit: '))
celsius = (farenheit-32)/1.8
print('{}ºF é igual a {}ºC'.format(farenheit, celsius))
