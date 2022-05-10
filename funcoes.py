import random
from math import*

def normaliza (dicionario):
    novo_dicionario = {}
    for continentes, informacoes_paises in dicionario.items():
        for paises, informacoes in informacoes_paises.items():
            informacoes['continente'] = continentes
            novo_dicionario[paises] = informacoes
    return novo_dicionario

def sorteia_paises(dicio_paises):
    paises=[]
    for i in paises.keys():
        paises.append(i)
    sorteado=random.choice(paises)

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
    
def esta_na_lista(pais, paises):
    x=0
    for Estado in paises:
        if pais ==Estado[0]:
            x=1
    if x==1:
        return True
    if x==0:
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