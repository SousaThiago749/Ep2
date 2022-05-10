def esta_na_lista(pais, paises):
    x=0
    for Estado in paises:
        if pais ==Estado[0]:
            x=1
    if x==1:
        return True
    if x==0:
        return False