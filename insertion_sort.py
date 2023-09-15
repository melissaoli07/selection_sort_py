#insertion sort - ordenação por inserção 
def insertion_sort(lista):
    for i in range (1, len(lista)):
        pivo = lista[i]
        j = i-1
        #j=0
        #while j < i and lista [j]>chave:
        while j>=0 and pivo<lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo     


#principal
lista = [12,12,13,5,6]
print(f'original: {lista}')
insertion_sort(lista)
print(f'ordenada: {lista}')