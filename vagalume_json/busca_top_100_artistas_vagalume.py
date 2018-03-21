import json
import requests

def remove_repetidos(lista):
    l = [] 
    for i in lista:
        if i not in l and len(i)> 3 and i != 'REFRÃO' and i != "100%":
            l.append(i)
    l.sort()
    return l

def busca_musicas(id_api):
    r = requests.get(id_api+'index.js')
    if r.status_code == 200:
        reddit_data = json.loads(r.content)
        musicas = reddit_data['artist']['lyrics']['item']
        for id_music in musicas:
            r2 = requests.get('https://api.vagalume.com.br/search.php?musid='+id_music['id'])
            if r2.status_code == 200:
                reddit_data = json.loads(r2.content)
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
                limpa_string = limpa_string.replace(':', '') # Retira DOIS PONTOS
                limpa_string = limpa_string.replace(';', '') # Retira PONTO E VIRGULA
                limpa_string = limpa_string.replace('"', '') # Retira aspas duplas
                lista = remove_repetidos(limpa_string.split())
                for d in lista:
                    btl = '\"'+ d+ '\", '
                    arquivo = open('musicas.txt','a')
                    arquivo.write(btl)
                    arquivo.close()
    print('Salvo com Sucesso!')


    
    
    
###########################################################################################################################


link_cantor = input('Informe o link do cantor no Vagalume.com: ')
busca_musicas(link_cantor)
    


    

        
        
