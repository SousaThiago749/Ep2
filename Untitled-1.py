from random import *
from math import*
import random


def sorteia_letra2 (palavra):
    letras = []
    palavra = palavra.lower()
    palavras_ja_sorteadas = []

    for i in palavra:
        letras.append(i)
    
    for j in letras:
        if j == ' ':
            letras = letras.replace(j, '')
                
    if palavra == '':
        return ''
        
    letra = random.choice(letras)
    
    while letra in palavras_ja_sorteadas:
        letra = random.choice(palavra)
    palavras_ja_sorteadas.append(letra)

    return palavras_ja_sorteadas

print(sorteia_letra2('japao'))