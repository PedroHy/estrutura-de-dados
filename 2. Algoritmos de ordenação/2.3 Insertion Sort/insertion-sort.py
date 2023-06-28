def insertion_sort(lista):
  # determina o tamanhho da lista
  list_size = len(lista)
  

  for i in range(1, list_size):
    # 
    key = lista[i]
    left = i - 1

    while left >= 0 and lista[left] > key:
      lista[left + 1] = lista[left]
      left -= 1
    lista[left+1] = key