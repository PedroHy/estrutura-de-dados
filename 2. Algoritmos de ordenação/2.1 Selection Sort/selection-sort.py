def selection_sort(lista):
  #determina o tamanhho da lista
  list_size = len(lista)
  
  #seleciona um elemento da lista por vez
  for i in range(list_size):
    lista[i]

    # compara o elemento selecionado com os outros da lista e se o elemento 
    # comparado for maior que o selecionado a posição deles é trocada
    for c in range(list_size):
      if lista[c] > lista[i]:
        lista[c], lista[i] = lista[i], lista[c]
   