def quick(array):
  if len(array)<=1:
    return array
  pivo = array[0]
  menores = [x for x in array[1:] if x <= pivo]
  maiores = [x for x in array[1:] if x > pivo]
  return quick(menores) + [pivo] + quick(maiores)