import random
import sys
import numpy as np

sys.setrecursionlimit(100000)

def bubbleSort(A):
    n = len(A)
    i = 0
    swapped = True

    while i < n - 1 and swapped:
        swapped = False

        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
                swapped = True

        i += 1

    return A

def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i

        while j > 0 and A[j - 1] > key:
            A[j] = A[j - 1]
            j -= 1

        A[j] = key

    return A

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        temp = A[i]
        A[i] = A[min_idx]
        A[min_idx] = temp

    return A

def mergeSort(A):
    mergeSortRecurse(A, 0, len(A) - 1)
    return A

def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2

        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)

def merge(A, leftIdx, midIdx, rightIdx):
    tempArr = np.empty(rightIdx - leftIdx + 1, dtype=A.dtype)
    ii = leftIdx
    jj = midIdx + 1
    kk = 0

    while ii <= midIdx and jj <= rightIdx:
        if A[ii] <= A[jj]:
            tempArr[kk] = A[ii]
            ii += 1
        else:
            tempArr[kk] = A[jj]
            jj += 1
        kk += 1

    for ii in range(ii, midIdx + 1):
        tempArr[kk] = A[ii]
        kk += 1

    for jj in range(jj, rightIdx + 1):
        tempArr[kk] = A[jj]
        kk += 1

    for kk in range(leftIdx, rightIdx + 1):
        A[kk] = tempArr[kk - leftIdx]

def quickSort(A):
    quickSortRecurse(A, 0, len(A) - 1)
    return A

def quickSortRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = leftIdx
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurse(A, leftIdx, newPivotIdx - 1)
        quickSortRecurse(A, newPivotIdx + 1, rightIdx)

def doPartitioning(A, leftIdx, rightIdx, pivIdx):
    pivotVal = A[pivIdx]
    A[pivIdx] = A[rightIdx]
    A[rightIdx] = pivotVal
    currIdx = leftIdx
    for ii in range(leftIdx, rightIdx):
        if A[ii] < pivotVal:
            temp = A[ii]
            A[ii] = A[currIdx]
            A[currIdx] = temp
            currIdx += 1

    newPivIdx = currIdx
    A[rightIdx] = A[newPivIdx]
    A[newPivIdx] = pivotVal

    return newPivIdx

def quickSortMedian3(A):
    quickSortMedian3Recurse(A, 0, len(A) - 1)
    return A

def quickSortMedian3Recurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = medianOfThree(A, leftIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortMedian3Recurse(A, leftIdx, newPivotIdx - 1)
        quickSortMedian3Recurse(A, newPivotIdx + 1, rightIdx)

def medianOfThree(A, leftIdx, rightIdx):
    midIdx = (leftIdx + rightIdx) // 2
    l = A[leftIdx]
    m = A[midIdx]
    r = A[rightIdx]

    if (l <= m and m <= r) or (r <= m and m <= l):
        result = midIdx
    elif (m <= l and l <= r) or (r <= l and l <= m):
        result = leftIdx
    else:
        result = rightIdx

    return result

def quickSortRandom(A):
    quickSortRandomRecurse(A, 0, len(A) - 1)
    return A

def quickSortRandomRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = random.randint(leftIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRandomRecurse(A, leftIdx, newPivotIdx - 1)
        quickSortRandomRecurse(A, newPivotIdx + 1, rightIdx)

