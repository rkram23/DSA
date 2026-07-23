def selection(arr):
    for i in range (len(arr)-1):
        for j in range (i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

if __name__ == "__main__":
    arr = [5,7,3,21,4,9,2]
    print(selection(arr))