import time
from DSAHeap import DSAHeap

FILENAME = "RandomNames7000.csv"


def testHeap():
    print("DSAHeap test")
    heap = DSAHeap()
    for ii in range(12):
        priority = (ii * 37 + 11) % 101
        heap.add(priority, "item" + str(ii))
    heap.display()
    print("Removing one value (the highest priority):")
    removed = heap.remove()
    print("  Removed:", removed)
    print("Heap after remove:")
    heap.display()
    print("Extracting in priority order:")
    prev = None
    inOrder = True
    while heap.getCount() > 0:
        entry = heap.remove()
        print(" ", entry)
        if prev is not None and entry.getPriority() > prev:
            inOrder = False
        prev = entry.getPriority()
    print("Extracted in descending order:", inOrder)


def testSlideExample():
    print("HeapSort slide example")
    heap = DSAHeap()
    for num in [5, 4, 1, 11, 10, 3, 2, 16, 12]:
        heap.addUnordered(num, str(num))
    heap.heapify()
    print("After heapify:", end=" ")
    for ii in range(heap.getCount()):
        print(heap.getEntry(ii).getPriority(), end=" ")
    print()
    heap.heapSort()
    print("After heapSort:", end=" ")
    for ii in range(heap.getCount()):
        print(heap.getEntry(ii).getPriority(), end=" ")
    print()


def firstIntField(line):
    start = 0
    for ii in range(len(line) + 1):
        if ii == len(line) or line[ii] == ",":
            try:
                return int(line[start:ii])
            except ValueError:
                start = ii + 1
    return None


def trimEnd(line):
    end = len(line)
    while end > 0 and (line[end - 1] == "\n" or line[end - 1] == "\r"):
        end -= 1
    return line[:end]


def loadFile(filename, heap):
    with open(filename, "r") as f:
        for line in f:
            text = trimEnd(line)
            number = firstIntField(text)
            if number is not None:
                heap.addUnordered(number, text)


def testFile(filename):
    print(f"HeapSort on {filename}")
    heap = DSAHeap()
    loadFile(filename, heap)
    n = heap.getCount()

    start = time.perf_counter()
    heap.heapSort()
    elapsed = time.perf_counter() - start

    ok = True
    for ii in range(n - 1):
        if heap.getEntry(ii).getPriority() > heap.getEntry(ii + 1).getPriority():
            ok = False
    print(f"Ordered {n} items in {elapsed:.4f}s - correct: {ok}")

    k = min(5, n)
    print("First 5:", end=" ")
    for ii in range(k):
        print(heap.getEntry(ii).getPriority(), end=" ")
    print()
    print("Last 5: ", end=" ")
    for ii in range(n - k, n):
        print(heap.getEntry(ii).getPriority(), end=" ")
    print()


if __name__ == "__main__":
    testHeap()
    testSlideExample()
    testFile(FILENAME)