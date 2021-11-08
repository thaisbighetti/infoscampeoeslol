import json
import requests

r = requests.get('http://ddragon.leagueoflegends.com/cdn/11.22.1/data/en_US/champion.json')
lol = r.json()
data = lol['data']

champ = []
blurb = []
tags = []
title = []
campeoes = []
diff = []
hp = []
movespeed = []
armor = []
mr = []


def separar_infos() :
    for champs in data :
        blurb.append((data[champs]['blurb']))
        champ.append(champs)
        tags.append(data[champs]['tags'])
        title.append(data[champs]['title'])
        diff.append(data[champs]['info']['difficulty'])
        hp.append(data[champs]['stats']['hp'])
        movespeed.append(data[champs]['stats']['movespeed'])
        armor.append(data[champs]['stats']['armor'])
        mr.append(data[champs]['stats']['spellblock'])


def juntando_infos() :
    for i in range(len(champ)) :
        dicio = {'Nome do Campeão' : champ[i],
                 'Título' : title[i],
                 'Frase' : blurb[i],
                 'Posição' : tags[i],
                 'Vida' : hp[i],
                 'Velocidade de Movimento' : movespeed[i],
                 'Armadura' : armor[i],
                 'Resistencia Mágica' : mr[i]}
        campeoes.append(dicio)


def criar_json() :
    campeoeslol = {'Campeões' : campeoes}
    dados_json = json.dumps(campeoeslol, indent=4)
    arquivo = open("campeoeslol.json", "w")
    arquivo.write(dados_json)
    arquivo.close()


def main() :
    separar_infos()
    juntando_infos()
    criar_json()


main()
print(campeoes)
