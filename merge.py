def mergesort(array, first=0, end=None):
  if end is None:
    end = len(array)
  if((end - first) > 1):
      mid = (end + first)//2
      mergesort(array, first, mid)
      mergesort(array, mid, end)
      merge(array, first, mid, end)
  return array

def merge(array, first, mid, end):
  left = array[first:mid]
  right = array[mid:end]
  i, j = 0, 0

  for k in range(first, end):
    if i >= len(left):
      array[k] = right[j]
      j+=1

    elif j >= len(right):
      array[k] = left[i]
      i+=1

    elif left[i]<=right[j]:
      array[k]=left[i]
      i+=1

    else:
      array[k] = right[j]
      j+=1
  return array
