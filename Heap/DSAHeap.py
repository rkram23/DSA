import numpy as np


class DSAHeapEntry:
    def __init__(self, priority, value):
        self.__priority = priority
        self.__value = value

    def getPriority(self):
        return self.__priority

    def setPriority(self, priority):
        self.__priority = priority

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def __str__(self):
        return f"({self.__priority}, {self.__value})"


class DSAHeap:
    def __init__(self, capacity=10):
        self.__heap = np.empty(capacity, dtype=object)
        self.__count = 0

    def getCount(self):
        return self.__count

    def getEntry(self, idx):
        return self.__heap[idx]

    def add(self, priority, value):
        if self.__count == self.__heap.shape[0]:
            self.__grow()
        self.__heap[self.__count] = DSAHeapEntry(priority, value)
        self.__trickleUp(self.__count)
        self.__count += 1

    def addUnordered(self, priority, value):
        if self.__count == self.__heap.shape[0]:
            self.__grow()
        self.__heap[self.__count] = DSAHeapEntry(priority, value)
        self.__count += 1

    def remove(self):
        if self.__count == 0:
            raise IndexError("Heap is empty")
        root = self.__heap[0]
        self.__count -= 1
        self.__heap[0] = self.__heap[self.__count]
        self.__heap[self.__count] = None
        self.__trickleDown(self.__heap, 0, self.__count)
        return root

    def display(self):
        for ii in range(self.__count):
            print(f"[{ii}] {self.__heap[ii]}")

    def heapify(self):
        for ii in range(self.__count // 2 - 1, -1, -1):
            self.__trickleDown(self.__heap, ii, self.__count)

    def heapSort(self):
        self.heapify()
        for ii in range(self.__count - 1, 0, -1):
            self.__swap(self.__heap, 0, ii)
            self.__trickleDown(self.__heap, 0, ii)

    def __trickleUp(self, curIdx):
        parentIdx = (curIdx - 1) // 2
        while curIdx > 0 and \
                self.__heap[curIdx].getPriority() > self.__heap[parentIdx].getPriority():
            self.__swap(self.__heap, curIdx, parentIdx)
            curIdx = parentIdx
            parentIdx = (curIdx - 1) // 2

    def __trickleDown(self, heapArray, curIdx, numItems):
        lChildIdx = curIdx * 2 + 1
        rChildIdx = lChildIdx + 1
        keepGoing = True
        while keepGoing and lChildIdx < numItems:
            keepGoing = False
            largeIdx = lChildIdx
            if rChildIdx < numItems:
                if heapArray[lChildIdx].getPriority() < heapArray[rChildIdx].getPriority():
                    largeIdx = rChildIdx
            if heapArray[largeIdx].getPriority() > heapArray[curIdx].getPriority():
                self.__swap(heapArray, largeIdx, curIdx)
                keepGoing = True
                curIdx = largeIdx
                lChildIdx = curIdx * 2 + 1
                rChildIdx = lChildIdx + 1

    def __swap(self, heapArray, idxA, idxB):
        temp = heapArray[idxA]
        heapArray[idxA] = heapArray[idxB]
        heapArray[idxB] = temp

    def __grow(self):
        bigger = np.empty(self.__heap.shape[0] * 2, dtype=object)
        for ii in range(self.__count):
            bigger[ii] = self.__heap[ii]
        self.__heap = bigger