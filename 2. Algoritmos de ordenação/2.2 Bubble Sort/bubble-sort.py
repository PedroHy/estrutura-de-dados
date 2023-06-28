def bubble_sort(list):
  # determina o tamanhho da lista
  list_size = len(list)

  # seleciona dois elementos adjacentes e faz a comparação entre eles, se o da
  # esquerda for maior que o da direita a posição deles é trocada
  for c in range(list_size - 2):
     for i in range(list_size - 2):
       if list[i] > list[i+1]:
          list[c], list[i] = list[i], list[c]