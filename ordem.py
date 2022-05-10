def adciona_em_ordem(pais,dist,lista):
    contador = 0
    pais_dist=[pais, dist]
    for x in lista:
        if dist >x[1]:
            contador = contador + 1
    lista.insert(contador, pais_dist)
    return lista