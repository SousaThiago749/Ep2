from random import *
from math import*

def normaliza (dicionario):
    novo_dicionario = {}
    for continentes, informacoes_paises in dicionario.items():
        for paises, informacoes in informacoes_paises.items():
            informacoes['continente'] = continentes
            novo_dicionario[paises] = informacoes
    return novo_dicionario

def sorteia_paises(dicio_paises):
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
    print('')
    print('Comandos:')
    print('     dica        - entra no mercado de dicas')
    print('     desisto     - desiste da rodada')
    print('     inventario  - exibe sua posição')
    
    
