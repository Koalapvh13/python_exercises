#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Altura: '))
peso_ideal = (72.7*altura) - 58
print('Seu peso ideal é {:.2f}Kg'.format(peso_ideal))
