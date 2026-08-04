#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    n = len(A)
    i = 0
    swapped = True

    while i < n - 1 and swapped:
        swapped = False

        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True

        i += 1

    return A 

def insertionSort(A):
    for i in range(1, len(A)):
       key = A[i]

       while A[i-1] > key and i > 0:
           A[i], A[i-1] = A[i-1], A[i]
           i = i - 1 
    return A

def selectionSort(A):
    for i in range (len(A)-1):
        for j in range (i+1, len(A)):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


