#contributed by Vedant
def binarySearch(arr, l, h, x):
    if h >= l:
        mid = l + (h - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, h, x)
    else:
        return -1

arr = [1 ,4 ,6 ,2 ,8 ,3 ,9]
x = 8
pos = binarySearch(arr, 0, len(arr)-1, x)
if pos != -1:
	print("Element is present at index ", pos)
else:
	print("Element is not present in array")