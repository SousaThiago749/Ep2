import random
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

print(sorteia_letra('Andorra a-Velha',  ['a', 'r']))