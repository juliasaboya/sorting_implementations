def insertion(array, posicao = 0):
  if(posicao < len(array)):
    for j in range(posicao, 0, -1):
      if (array[j]<array[j-1]):
        array[j], array[j-1] = array[j-1], array[j]
    insertion(array, posicao + 1)
  return array

array = [8,7,5,1,22]
insertion(array)
print(array)