#Faça um Programa que pergunte quanto você ganha por hora e
#o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('Quanto ganha por hora? R$ '))
tempo_trabalhado = float(input('Quantas horas trabalhadas? '))
salario_total = salario_hora*tempo_trabalhado
print('Seu salário será de R$ {:.2f}'.format(salario_total))
