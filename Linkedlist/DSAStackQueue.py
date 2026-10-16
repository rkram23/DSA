"""
Citation: DSAStack and DSAQueue redeveloped from my own Practical 3 submission (Ramkumar Arumugam, Student ID 23811719) - array-based push/pop/enqueue/dequeue logic reused here, to call
DSALinkedList instead of an array.
"""
from DSALinkedList import DSALinkedList


class DSAStack:

    def __init__(self):
        self._list = DSALinkedList()

    def push(self, value):
        self._list.insertFirst(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty - cannot pop")
        value = self._list.peekFirst()
        self._list.removeFirst()
        return value

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty - cannot peek")
        return self._list.peekFirst()

    def isEmpty(self):
        return self._list.isEmpty()

    def getCount(self):
        return self._list.getCount()


class DSAQueue:

    def __init__(self):
        self._list = DSALinkedList()

    def enqueue(self, value):
        self._list.insertLast(value)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty - cannot dequeue")
        value = self._list.peekFirst()
        self._list.removeFirst()
        return value

    def peek(self): #prac3
        if self.isEmpty():
            raise Exception("Queue is empty - cannot peek")
        return self._list.peekFirst()

    def isEmpty(self):
        return self._list.isEmpty()

    def getCount(self):
        return self._list.getCount()


def main():
    choice = input("s / q ? ").strip().lower()

    if choice == "s":
        s = DSAStack()
        while True:
            print("\n1. push \n2. Pop \n3. Display\n0. Exit")
            option = input("Enter choice: ").strip()

            if option == "1":
                value = input("Enter value to push: ")
                s.push(value)
                print(f"Pushed '{value}'.")

            elif option == "2":
                try:
                    print(f"Popped: {s.pop()}")
                except Exception as e:
                    print(f"Error: {e}")

            elif option == "3":
                if s.isEmpty():
                    print("(empty stack)")
                else:
                    current = s._list._head
                    output = "[Top] "
                    while current is not None:
                        output += str(current.getValue())
                        if current.getNext() is not None:
                            output += " -> "
                        current = current.getNext()
                    print(output)

            elif option == "0":
                return

            else:
                print("Invalid choice, try again.")

    elif choice == "q":
        q = DSAQueue()
        while True:
            print("\n1. Enqueue\n2. Dequeue \n3. Display\n0. Exit")
            option = input("Enter choice: ").strip()

            if option == "1":
                value = input("Enter value to enqueue: ")
                q.enqueue(value)
                print(f"Enqueued '{value}'.")

            elif option == "2":
                try:
                    print(f"Dequeued: {q.dequeue()}")
                except Exception as e:
                    print(f"Error: {e}")

            elif option == "3":
                if q.isEmpty():
                    print("(empty queue)")
                else:
                    current = q._list._head
                    output = "[Front] "
                    while current is not None:
                        output += str(current.getValue())
                        if current.getNext() is not None:
                            output += " -> "
                        current = current.getNext()
                    print(output)

            elif option == "0":
                return

            else:
                print("Invalid choice, try again.")

    else:
        print("Invalid choice - enter 's' or 'q'.")


if __name__ == "__main__":
    main()