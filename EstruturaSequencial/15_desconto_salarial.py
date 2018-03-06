# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#  11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

import os

salario_hora = float(input('Ganho por hora: R$ '))
horas_trabalhadas = float(input('Horas trabalhadas: '))

salario_mensal = salario_hora*horas_trabalhadas
ir = salario_mensal*0.11
inss = salario_mensal*0.08
sindicato = salario_mensal*0.05
salario_liquido = salario_mensal - (ir+inss+sindicato)

print('\n\n\n\n+Salário Bruto: R$ {:.2f}\n-IR (11%): R$ {:.2f}\n'
      '-INSS (8%): R$ {:.2f}\n-Sindicato (5%): R$ {:.2f}\n=Salário Liquido: R$: {}'
      .format(salario_mensal, ir, inss, sindicato, salario_liquido))

os.system("pause")

