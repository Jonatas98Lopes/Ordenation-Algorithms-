def troca(lista, indice1, indice2):
    temporario = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = temporario

def empurra(lista, tamanho):
    for i in range(tamanho - 1):
        if lista[i] > lista[i + 1]:
            troca(lista, i, (i + 1))

def bubble_sort(lista):
    tamanho = len(lista)
    while tamanho > 1:
        empurra(lista, tamanho)
        tamanho -= 1


lista = [54, 5, 23, 13, 25, 1, 256, 3]
print(lista)
print()
bubble_sort(lista)
print(lista)
