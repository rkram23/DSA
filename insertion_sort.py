def insertion(arr):

    for i in range(1, len(arr)):
       key = arr[i]

       while arr[i-1] > key and i > 0:
           arr[i], arr[i-1] = arr[i-1], arr[i]
           i = i - 1 
    return arr


arr = [8,4,6,2,5,4,9,1]

print(insertion(arr))