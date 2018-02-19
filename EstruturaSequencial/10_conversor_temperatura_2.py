#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celsius = float(input('Celsius: '))
farenheit = (1.8*celsius)+32
print('{}ºC equivale a {:.1f}ºF'.format(celsius, farenheit))

