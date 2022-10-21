# Bubble sort (Ascending) Implementation
def bubbleSort(arr):   
  # Traverse through all the array elements
  for ps in range(len(arr)):
    # loop to compare array elements
    for j in range(0, len(arr) - ps - 1):
      # compare two adjacent elements
      # change > to < to sort in descending order
      if arr[j] > arr[j + 1]:
        # swapping elements if elements
        # are not in the intended order
        tmp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp


arr = [10, -2 , -10, 4, 9, 100]

bubbleSort(arr)

print('The sorted array is :')
print(data)