from DSALinkedList import DSALinkedList


def menu():
    myList = DSALinkedList()

    menuText = """
--- DSALinkedList Menu ---
1. Insert First
2. Insert Last
3. Remove First
4. Remove Last
5. Peek First
6. Peek Last
7. Display List
0. Exit
"""

    while True:
        print(menuText)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = input("Enter value to insert at front: ")
            myList.insertFirst(value)
            print(f"Inserted '{value}' at front.")

        elif choice == "2":
            value = input("Enter value to insert at end: ")
            myList.insertLast(value)
            print(f"Inserted '{value}' at end.")

        elif choice == "3":
            try:
                removed = myList.removeFirst()
                print(f"Removed from front: {removed}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            try:
                removed = myList.removeLast()
                print(f"Removed from end: {removed}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            try:
                print(f"First value: {myList.peekFirst()}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            try:
                print(f"Last value: {myList.peekLast()}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "7":
            myList.display()

        elif choice == "0":
            print("Exiting.")
            return

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()