#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quadrado = float(input('Informe a medida de um dos lados do quadrado: '))
area = quadrado*quadrado
print('o quadrado possui área de {} cm², e o dobro dessa área é {} cm².'.format(area, (area*2)))
