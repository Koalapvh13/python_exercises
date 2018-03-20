import json # Importa o módulo que faz a leitura do JSON
import requests # Importa o módulo que faz a requisição HTTP do JSON

 # Remove todos os itens repitidos do array anterior
def remove_repetidos(lista):
    l = [] 
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


# Salva as Strings no BD    
def pega_letra(link_json):

    r = requests.get(link_json)
    if r.status_code == 200:
        reddit_data = json.loads(r.content)
        limpa_string = reddit_data['mus'][0]['text'].replace('.', '') # Retira ponto final
        limpa_string = limpa_string.replace(',', '') # Retira virgula
        limpa_string = limpa_string.replace('?', '') # Retira ponto de interrogação
        limpa_string = limpa_string.replace('!', '') # Retira ponto de exclamação
        limpa_string = limpa_string.replace('(', '') # Retira abre parênteses
        limpa_string = limpa_string.replace(')', '') # Retira fecha parênteses
        limpa_string = limpa_string.replace('[', '') # Retira abre colchetes
        limpa_string = limpa_string.replace(']', '') # Retira fecha colchetes
        limpa_string = limpa_string.replace('{', '') # Retira abre chaves 
        limpa_string = limpa_string.replace('}', '') # Retira fecha chaves
        limpa_string = limpa_string.replace('/', '') # Retira barra
        limpa_string = limpa_string.replace('"', '') # Retira aspas duplas
        lista = remove_repetidos(limpa_string.split())
    return lista


###########################################################################################
# PROGRAMA PRINCIPAL

r = 'https://api.vagalume.com.br/search.php?musid=3ade68b8gfe4890b3'

print(pega_letra(r))
for d in pega_letra(r):
    btl = '\"'+ d+ '\", '
    arquivo = open('letras.txt','a')
    arquivo.write(btl)
    arquivo.close()
    
