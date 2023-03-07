def troca(lista, indice1, indice2):
    temporario = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = temporario

def insertion_sort(lista):
    for x in range(1, len(lista)):
        valor = lista[x]
        i = lista.index(valor) - 1
        while i >= 0:
            if lista[i] > valor:
                troca(lista, lista.index(valor), lista.index(lista[i]))
            i -= 1
        
lista = [23, 3, 12, 234, 2, 43]
print(lista)
print()
insertion_sort(lista)
print(lista)
