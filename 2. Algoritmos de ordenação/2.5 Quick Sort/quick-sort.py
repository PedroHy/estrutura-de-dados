def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        # Seleciona o pivô como o primeiro elemento da lista
        pivo = lista[0]
        
        # Separa a lista em duas partes: elementos menores que o pivô e maiores ou iguais ao pivô
        menores = [x for x in lista[1:] if x < pivo]
        maiores = [x for x in lista[1:] if x >= pivo]
        
        # Ordena as duas partes separadamente e retorna a lista ordenada
        return quick_sort(menores) + [pivo] + quick_sort(maiores)