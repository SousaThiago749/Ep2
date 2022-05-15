from random import *
from math import*
import random
from termcolor import colored

def normaliza (dicionario):
    novo_dicionario = {}
    for continentes, informacoes_paises in dicionario.items():
        for paises, informacoes in informacoes_paises.items():
            informacoes['continente'] = continentes
            novo_dicionario[paises] = informacoes
    return novo_dicionario

def sorteia_pais(dicio_paises):
    paises = list(dicio_paises.keys())
    paisSorteado = choice(paises)
    return paisSorteado

def haversine(raio, lat1, long1, lat2, long2):
  lat1 = radians(lat1) 
  lat2 = radians(lat2) 
  long1 = radians(long1) 
  long2 = radians(long2) 

  a = sin((lat2-lat1)/2)**2
  b = cos(lat1)*cos(lat2)
  c = sin((long2-long1)/2)**2 

  raiz = sqrt(a + (b*c))

  distancia = 2*raio*asin(raiz)

  return distancia

def pega_lat_long_de_pais(dadosnormalizados, pais_sorteado, resposta):
    lat_resposta = dadosnormalizados[resposta]['geo']['latitude']
    long_resposta = dadosnormalizados[resposta]['geo']['longitude']
    lat_sorteado = dadosnormalizados[pais_sorteado]['geo']['latitude']
    long_sorteado = dadosnormalizados[pais_sorteado]['geo']['longitude']

    return lat_resposta, long_resposta, lat_sorteado, long_sorteado    

def adciona_em_ordem(resposta,dist,lista_chutes):
    contador = 0
    pais_dist=[resposta, dist]
    for x in lista_chutes:
        if dist >x[1]:
            contador = contador + 1
    lista_chutes.insert(contador, pais_dist) #ou lista_chutes[contador] = pais_dist
    return lista_chutes

def ordem_das_distancias(distancias):
    
    lista_dist = []

    for dict in distancias.values():
        lista_dist.append(dict['distancia'])

    lista_dist.sort()

    novo_dict = {}

    i = 0

    while i != len(lista_dist):
        for guess, dic in distancias.items():
            if (dic['distancia'] == lista_dist[i]):
                novo_dict[guess] = {'distancia': dic['distancia'], 'cor' : dic['cor']}

        i+=1

    return novo_dict


    
def esta_na_lista (pais, lista):
    esta = 0
    for i in lista:
        if pais == i:
            esta = 1
    if esta == 1:
        return True
    else:
        return False

def sorteia_letra (palavra, lista_restrita):
    especiais = ['.', ',', '-', ';', ' ', "'"]
    palavra = palavra.lower()
    
    for i in lista_restrita:
        especiais.append(i)
    
    for j in palavra:
        if j in especiais:
            palavra = palavra.replace(j, '')
                
    if palavra == '':
        return ''
        
    letra = random.choice(palavra)
    
    while letra in especiais:
        letra = random.choice(palavra)
        
    return letra

def DesenhaInterface():
    print(' ============================')
    print('|                            |')
    print('| Bem vindo ao Insper Países |')
    print('|                            |')
    
    print(' ==== Design de Software ====')

    print('\n')
    print('Comandos:')
    print('     dica        - entra no mercado de dicas')
    print('     desisto     - desiste da rodada')
    print('     inventario  - exibe sua posição')

def desenha_menu_dicas(dict_opcoes, tentativas):

    print('Mercado de Dicas')
    print('----------------------------------------')
    
    for nome, tentativa in dict_opcoes.items():
        if tentativa < tentativas:
            print(nome + ' - custa ' + str(tentativa) + ' tentativas')

    print('----------------------------------------')

def mostra_inventario(lista_cor_bandeira, dict_distancias, lista_letras_capitais, lista_area, novo_dict):
    print('')
    print('Distâncias: ')
    
    for pais_chutado, dic_valor in dict_distancias.items():
        print("     " + str(int(dic_valor['distancia'])) + ' km -> ' + pais_chutado)
        print("")

    print('Dicas: ')
    if len(lista_cor_bandeira) != 0: 
        print('\n - Cores da bandeira: ', end='')
        for dica in lista_cor_bandeira:
            print(dica + ', ', end='')

    if len(lista_letras_capitais) != 0:
        print('\n - Letras da capital: ', end='')
        for letra in lista_letras_capitais:
            print(letra + ', ', end='')

    if len(lista_area) != 0:
        print('\n - Área: ' + str(lista_area[0]) + ' km²')
    
    print('')
        
    
def mostra_dica_escolhida(dica, dados, pais, lista_cores_dicas, lista_area, lista_letras_capital):
    if dica == '1':
        lista_cores = []
        for cor in dados[pais]['bandeira'].keys():
            lista_cores.append(cor)

        cor = choice(lista_cores)

        while cor in lista_cores_dicas:
            cor = choice(lista_cores)

        lista_cores_dicas.append(cor)
        return 4

    elif dica == '2':
        tamanho_capital = len(dados[pais]['capital'])

        if len(lista_letras_capital) < tamanho_capital:
            letra_sorteada = sorteia_letra_capital(dados, pais, lista_letras_capital)
            lista_letras_capital.append(letra_sorteada)
        return 3
    
    elif dica == '3':
        if len(lista_area) == 0:
            area = dados[pais]['area']
            lista_area.append(area)
        return 6

    elif dica == '4':
        dica_populacao = False
        if dica_populacao == False:
            pop = dados[pais]['populacao']
            dica_populacao == True
            return pop
        else:
            return None

    elif dica == '5':
        dica_continente = False
        if dica_continente == True:
            continente = dados.keys()
            dica_continente == True
            return continente
        else:
            return None
    
    elif dica == '0':
        return

def sorteia_letra_capital(dados, pais, lista_letras):
    especiais = ['.', ',', '-', ';', ' ', "'"]

    capital = dados[pais]['capital'].lower()

    for especial in especiais:
        capital = capital.replace(especial, '')
        
    letra = choice(capital)

    while letra in lista_letras:
        letra = choice(capital)

    return letra

def tamanho_capital(dados, pais):
    especiais = ['.', ',', '-', ';', ' ', "'"]

    capital = dados[pais]['capital'].lower()

    for especial in especiais:
        capital = capital.replace(especial, '')
        
    return len(capital)

def devolve_opcoes_validas(lista_area, lista_cor_bandeira, tamanho_lista_cores, lista_letra_capital, tamanho_capital):
    dict = {}

    if len(lista_cor_bandeira) < tamanho_lista_cores:
        dict['1. Cor da Bandeira'] =  4

    if len(lista_letra_capital) < tamanho_capital:
        dict['2. Letra da capital'] =  3

    if len(lista_area) == 0:
        dict['3. Área'] =  6
    


    return dict
