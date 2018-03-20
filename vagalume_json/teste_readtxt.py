import json
import requests
 # Remove todos os itens repitidos do array anterior
def remove_repetidos(lista):
    l = [] 
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

arquivo = open('letras.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
