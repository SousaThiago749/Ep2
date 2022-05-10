def normaliza (dicionario):
    novo_dicionario = {}
    for continentes, informacoes_paises in dicionario.items():
        for paises, informacoes in informacoes_paises.items():
            informacoes['continente'] = continentes
            novo_dicionario[paises] = informacoes
    return novo_dicionario