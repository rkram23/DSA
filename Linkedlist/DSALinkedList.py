class DSAListNode:

    def __init__(self, value):
        self._value = value
        self._next = None
        self._prev = None

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, node):
        self._next = node

    def getPrev(self):
        return self._prev

    def setPrev(self, node):
        self._prev = node


class DSALinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def isEmpty(self):
        return self._head is None

    def getCount(self):
        return self._count

    def insertFirst(self, value):
        newNode = DSAListNode(value)
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode.setNext(self._head)
            self._head.setPrev(newNode)
            self._head = newNode
        self._count += 1

    def insertLast(self, value):
        newNode = DSAListNode(value)
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode.setPrev(self._tail)
            self._tail.setNext(newNode)
            self._tail = newNode
        self._count += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty - cannot removeFirst")

        removedNode = self._head
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.getNext()
            self._head.setPrev(None)

        self._count -= 1
        removedNode.setNext(None)
        return removedNode.getValue()

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty - cannot removeLast")

        removedNode = self._tail
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.getPrev()
            self._tail.setNext(None)

        self._count -= 1
        removedNode.setPrev(None)
        return removedNode.getValue()

    def peekFirst(self):
        if self.isEmpty():
            raise Exception("List is empty - cannot peekFirst")
        return self._head.getValue()

    def peekLast(self):
        if self.isEmpty():
            raise Exception("List is empty - cannot peekLast")
        return self._tail.getValue()

    def display(self):
        if self.isEmpty():
            print("(empty list)")
            return

        current = self._head
        output = ""
        while current is not None:
            output += str(current.getValue())
            if current.getNext() is not None:
                output += " <-> "
            current = current.getNext()
        print(output)


def main():
    l = DSALinkedList()
    while True:
        print("\n1. Insert at First\n2. Insert at Last\n3. Remove at First\n4. Remove at Last\n5. Display\n0. Exit")
        option = input("Enter choice: ").strip()

        if option == "1":
            value = input("Enter value to insert at front: ")
            l.insertFirst(value)
            print(f"Inserted '{value}' at front.")

        elif option == "2":
            value = input("Enter value to insert at end: ")
            l.insertLast(value)
            print(f"Inserted '{value}' at end.")

        elif option == "3":
            try:
                print(f"Removed: {l.removeFirst()}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "4":
            try:
                print(f"Removed: {l.removeLast()}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == "5":
            l.display()

        elif option == "0":
            return

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()