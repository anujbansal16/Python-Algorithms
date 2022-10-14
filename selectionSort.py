def selectionSort(arr):

    for i in range(len(arr)): 
        min_index = i 
        for j in range(i+1, len(arr)): 
            if arr[min_index] > arr[j]: 
                min_index = j       
        arr[i], arr[min_index] = arr[min_index], arr[i] 
    return arr

if __name__ == "__main__":
    marks = [22,66,43,58,98,42,77,56,66]
    result = selectionSort(marks)

    print(result)
