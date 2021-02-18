# def bubbleSort(arr):
#   n = len(arr)

#   for i in range(n):
#     for j in range(0, n-i-1):
#       if arr[j] > arr[j+1]:
#         arr[j], arr[j+1] = arr[j+1], arr[j]
#   return arr

# arr = [64, 34, 25, 12, 22, 11, 90]

# print(bubbleSort(arr))

# def selectionSort(arr):
#   for i in range(len(arr)):
#     min_idx = i
#     for j in range(i+1, len(arr)):
#       if arr[min_idx] > arr[j]:
#         min_idx = j
    
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]

#   return arr


# arr = [64, 25, 12, 22, 11]
# print(selectionSort(arr))

def multikeySort(arr):
  for j in range(len(arr)):
    for i in range(0, len(arr)-j-1):
      if arr[i][1] > arr[i+1][1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
      elif arr[i][1] == arr[i+1][1]:
        if arr[i][0] > arr[i+1][0]:
          arr[i], arr[i+1] = arr[i+1], arr[i]

  return arr


arr = [("Ben", "Cossum"), ("Ken", "Cossum"), ("John", "Stamos"), ("Rebecca", "Cossum"), ("Stephanie", "Parker"), ("Craig", "Paker"), ("Samantha", "Cossum"), ("Nick", "Cossum")]

print(multikeySort(arr))