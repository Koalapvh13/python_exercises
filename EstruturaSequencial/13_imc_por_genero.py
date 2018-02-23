#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

sexo = input('Qual o seu sexo?[M/F]: ')


if sexo != 'M' and 'F':
    print('Sexo inválido!')
elif sexo == 'M' or 'm':
    altura = float(input('Qual a sua altura: '))
    peso = float(input('Quanto você pesa: '))
    masc_formula = (72.7*altura)-58
    if peso > masc_formula:
        print('Seu peso ideal é {:.2f}Kg, você está acima do peso. Perca {:.2f}Kg.'.format(masc_formula, (peso - masc_formula)))
    elif peso == masc_formula:
        print('Seu peso ideal é {:.2f}Kg, você está no peso certo. Parabéns!'.format(masc_formula))
    else:
        print('Seu peso ideal é {:.2f}Kg, você está abaixo do peso. Ganhe {:.2f}Kg.'.format(masc_formula, (masc_formula - peso)))
elif sexo == 'F' or 'f':
    altura = float(input('Qual a sua altura: '))
    peso = float(input('Quanto você pesa: '))
    fem_formula = (62.1*altura)-44.7
    if peso > fem_formula:
        print('Seu peso ideal é {:.2f}Kg, você está acima do peso. Perca {:.2f}Kg.'.format(fem_formula, (peso - fem_formula)))
    elif peso == fem_formula:
        print('Seu peso ideal é {:.2f}Kg, você está no peso certo. Parabéns!'.format(fem_formula))
    else:
        print('Seu peso ideal é {:.2f}Kg, você está abaixo do peso. Ganhe {:.2f}Kg.'.format(fem_formula, (fem_formula - peso)))
else:
    print('Favor, refazer o processo')
