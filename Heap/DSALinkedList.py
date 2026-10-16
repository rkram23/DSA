class DSAListNode:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def getNext(self):
        return self.__next

    def setNext(self, node):
        self.__next = node

    def getPrev(self):
        return self.__prev

    def setPrev(self, node):
        self.__prev = node


class DSALinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
        self.__cursor = None        # last node accessed
        self.__cursorPos = 0        # its position

    def getCount(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def insertLast(self, value):
        node = DSAListNode(value)
        if self.__count == 0:
            self.__head = node
        else:
            self.__tail.setNext(node)
            node.setPrev(self.__tail)
        self.__tail = node
        self.__count += 1

    def takeLast(self):
        if self.__count == 0:
            raise IndexError("List is empty")
        value = self.__tail.getValue()
        if self.__count == 1:
            self.__head = None
            self.__tail = None
        else:
            newTail = self.__tail.getPrev()
            newTail.setNext(None)
            self.__tail.setPrev(None)
            self.__tail = newTail
        self.__count -= 1
        self.__cursor = None        
        return value

    def getAt(self, pos):
        return self.__nodeAt(pos).getValue()

    def setAt(self, pos, value):
        self.__nodeAt(pos).setValue(value)

    def swap(self, posA, posB):
        nodeA = self.__nodeAt(posA)
        nodeB = self.__nodeAt(posB)
        temp = nodeA.getValue()
        nodeA.setValue(nodeB.getValue())
        nodeB.setValue(temp)

    def __nodeAt(self, target):
        if target < 0 or target >= self.__count:
            raise IndexError("Position out of range")

        node = self.__head
        pos = 0
        best = target                              

        distTail = self.__count - 1 - target       
        if distTail < best:
            node = self.__tail
            pos = self.__count - 1
            best = distTail

        if self.__cursor is not None:
            distCursor = target - self.__cursorPos
            if distCursor < 0:
                distCursor = -distCursor
            if distCursor < best:
                node = self.__cursor
                pos = self.__cursorPos

        while pos < target:
            node = node.getNext()
            pos += 1
        while pos > target:
            node = node.getPrev()
            pos -= 1

        self.__cursor = node
        self.__cursorPos = target
        return node
