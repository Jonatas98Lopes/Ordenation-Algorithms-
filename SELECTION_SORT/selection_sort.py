def troca(lista, indice1, indice2):
    temporario = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = temporario

def pega_menor(lista, inicio):
    menor = min(lista[inicio:])
    return (lista.index(menor))

def selection_sort(lista):
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        minimo = pega_menor(lista, inicio)
        troca(lista, minimo, inicio)
        inicio += 1

lista = [23, 3, 12, 234, 2, 43]
print(lista)
print()
selection_sort(lista)
print(lista)
