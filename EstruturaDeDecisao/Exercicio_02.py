# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
numero = int(input('Informe um número inteiro: '))
if numero<0:
    print('O número',numero,'é NEGATIVO.')
elif numero==0:
    print('O número',numero,'é NEUTRO.')
else:
    print('O número',numero,'é POSITIVO.')
