# João Papo-de-Pescador, homem de bem,
# comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido
#  pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
#  Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

peso = float(input('O peixe pesa: '))
peso_maximo = 50
excesso = peso - peso_maximo
multa = excesso*4.0
if peso > peso_maximo:
    print('Seu peixe pesa {:.2f}Kg, {:.2f}Kg acima do permitido. Sua multa será de R$ {:.2f}.'.format(peso, excesso, multa))
else:
    print('Seu peixe pesa {:.2f}Kg, 0Kg acima do permitido. Sua multa será de R$ 0,00.'.format(peso))
