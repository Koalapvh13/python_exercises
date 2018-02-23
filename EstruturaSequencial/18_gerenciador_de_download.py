# Faça um programa que peça o tamanho de um arquivo para download (em MB) e
# a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade = float(input('Informe a velocidade de download (em Mbps): '))
tempo = (tamanho/velocidade)*60
print('Tempo de download estimado: {:.0f} minutos'.format(tempo))
