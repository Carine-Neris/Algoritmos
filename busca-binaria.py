"""
Pesquisa binária é um algoritmo de busca. A sua entrada é uma lista ordenada de elementos, 
se o elemento buscado estiver na lista, recebemos como resposta a posição que aquele elemento
se encontra, caso contrário a pesquisa retorna None
"""


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


lista = [1, 2, 3, 4, 10, 20, 55, 98]

print(pesquisa_binaria(lista, 10))
