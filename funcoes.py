from random import *
from math import*

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
    

def adciona_em_ordem(pais,dist,lista):
    contador = 0
    pais_dist=[pais, dist]
    for x in lista:
        if dist >x[1]:
            contador = contador + 1
    lista.insert(contador, pais_dist)
    return lista
    
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

def desenha_menu_dicas():

    print('Mercado de Dicas')
    print('----------------------------------------')
    print('1. Cor da bandeira  - custa 4 tentativas')
    print('2. Letra da capital - custa 3 tentativas')
    print('3. Área             - custa 6 tentativas')
    print('4. População        - custa 5 tentativas')
    print('5. Continente       - custa 7 tentativas')
    print('0. Sem dica')
    print('----------------------------------------')

def mostra_inventario(lista_cor_bandeira, dict_distancias):
    print('')
    print('Distâncias: ')
    
    for pais_chutado, dic_valor in dict_distancias.items():
        print("     " + str(int(dic_valor['distancia'])) + ' km -> ' + pais_chutado)
        print("")

    print('Dicas: ')
    if len(lista_cor_bandeira) != 0: 
        print(' - Cores da bandeira: ', end='')
        for dica in lista_cor_bandeira:
            print(dica, end='')
    
    print('')
        
    
def mostra_dica_escolhida(dica, dados, pais, lista_cores_dicas):

    if dica == '1':
        lista_cores = []
        for cor in dados[pais]['bandeira'].keys():
            lista_cores.append(cor)

        cor = choice(lista_cores)

        while cor in lista_cores_dicas:
            cor = choice(lista_cores)

        return cor

    if dica == '2':
        print()



    
