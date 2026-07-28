def bubble_sort(arr):
    n = len(arr)
    i = 0
    swapped = True

    while i < n - 1 and swapped:
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        i += 1

    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(bubble_sort(arr))
    arr2 = [5, 7, 3, 21, 4, 9, 2]
    print(bubble_sort(arr2))