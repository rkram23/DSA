import numpy as np
import sys
import timeit
import DSAsorts
import random

REPEATS = 3
NEARLY_PERCENT = 0.10
RANDOM_TIMES = 100

def usage():
    print(" Usage: python3 SortsTestHarness.py n xy [xy ...]")
    print("        where")
    print("        n is number of integers to sort")
    print("        x is one of")
    print("           b - bubblesort")
    print("           i - insertion sort")
    print("           s - selection sort")
    print("           m - mergesort")
    print("           q - quicksort (left-most pivot)")
    print("           t - quicksort (median-of-three pivot)")
    print("           r - quicksort (random pivot)")
    print("        y is one of")
    print("           a - 1..n ascending")
    print("           d - 1..n descending")
    print("           r - 1..n in random order")
    print("           n - 1..n nearly sorted (10% moved)")
def sortName(sortType):
    if sortType == "b":
        name = "Bubble"
    elif sortType == "i":
        name = "Insertion"
    elif sortType == "s":
        name = "Selection"
    elif sortType == "m":
        name = "MergeSort"
    elif sortType == "q":
        name = "QuickSort (left)"
    elif sortType == "t":
        name = "QuickSort (median3)"
    elif sortType == "r":
        name = "QuickSort (random)"
    else:
        name = "Unsupported sort algorithm"
    return name

def arrayName(arrayType):
    if arrayType == "a":
        name = "Ascending"
    elif arrayType == "d":
        name = "Descending"
    elif arrayType == "r":
        name = "Random"
    elif arrayType == "n":
        name = "Nearly sorted"
    elif arrayType == "u":
        name = "Duplicates"
    else:
        name = "Unsupported array type"
    return name

def makeArray(n, arrayType):
    A = np.arange(1, n+1, 1)

    if arrayType == 'a':
        pass
    elif arrayType == 'd':
        for i in range(0, int(n/2)):
            temp = A[i]
            A[i] = A[n-i-1]
            A[n-i-1] = temp
    elif arrayType == 'r':
        for i in range(RANDOM_TIMES*n):
            x = int(random.random()*n)
            y = int(random.random()*n)
            temp = A[x]
            A[x] = A[y]
            A[y] = temp
    elif arrayType == 'n':
        for i in range(int(n*NEARLY_PERCENT/2+1)):
            x = int(random.random()*n)
            y = int(random.random()*n)
            temp = A[x]
            A[x] = A[y]
            A[y] = temp
    elif arrayType == 'u':
        for i in range(n):
            A[i] = int(random.random()*5) + 1
    else:
        raise ValueError("Unsupported array type: " + arrayType)
    return A

def runSort(A, sortType):
    if sortType == "b":
        DSAsorts.bubbleSort(A)
    elif sortType == "i":
        DSAsorts.insertionSort(A)
    elif sortType == "s":
        DSAsorts.selectionSort(A)
    elif sortType == "m":
        DSAsorts.mergeSort(A)
    elif sortType == "q":
        DSAsorts.quickSort(A)
    elif sortType == "t":
        DSAsorts.quickSortMedian3(A)
    elif sortType == "r":
        DSAsorts.quickSortRandom(A)
    else:
        raise ValueError("Unsupported sort algorithm: " + sortType)

def timeSort(n, sortType, arrayType, show=False):
    A = makeArray(n, arrayType)

    if show:
        print("Generated array (" + arrayName(arrayType) + "): " +
              str(A.tolist()))

    startTime = timeit.default_timer()
    runSort(A, sortType)
    endTime = timeit.default_timer()

    for i in range(n-1):
        if A[i] > A[i+1]:
            raise ValueError("Array not in order")

    if show:
        print("Sorted array    (" + sortName(sortType) + "): " +
              str(A.tolist()))

    return endTime - startTime

def averageTime(n, sortType, arrayType):
    runningTotal = 0
    for repeat in range(REPEATS):
        # Print arrays on the first run only
        t = timeSort(n, sortType, arrayType, show=(repeat == 0))
        if repeat > 0:
            runningTotal += t
    return runningTotal/(REPEATS - 1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
    else:
        try:
            n = int(sys.argv[1])
            if n < 1:
                raise ValueError
        except ValueError:
            print("Error: n must be a positive integer, got '" +
                  sys.argv[1] + "'")
            usage()
            sys.exit(1)

        for aa in range(2, len(sys.argv)):
            arg = sys.argv[aa]
            try:
                if len(arg) != 2:
                    raise ValueError("Invalid argument '" + arg +
                                     "': expected two letters, e.g. br")
                sortType = arg[0]
                arrayType = arg[1]
                print(sortType + arrayType + " " + str(n) + " " +
                      str(averageTime(n, sortType, arrayType)))
            except ValueError as e:
                print("Error: " + str(e))
                usage()
                break