from DSAStack import DSAStack
from DSAQueue import DSAShufflingQueue, DSACircularQueue
from EquationSolver import EquationSolver


def get_push_number():
    valid = False
    number = 0
    while not valid:
        value = input("Enter a number to push: ")
        if value.isdigit():
            number = int(value)
            valid = True
        else:
            print("Invalid input, please enter an integer.")
    return number


def get_enqueue_number():
    valid = False
    number = 0
    while not valid:
        value = input("Enter a number to enqueue: ")
        if value.isdigit():
            number = int(value)
            valid = True
        else:
            print("Invalid input, please enter an integer.")
    return number


def test_stack():
    print("\n--- Testing DSAStack ---")
    s = DSAStack(20)
    running = True

    while running:
        print("\n1. Push")
        print("2. Pop")
        print("3. Top")
        print("4. isEmpty")
        print("5. Size (count)")
        print("6. Display stack")
        print("7. Back to main menu")
        choice = input("Enter choice: ")

        if choice == "1":
            value = get_push_number()
            s.push(value)
            print("Pushed", value)

        elif choice == "2":
            if s.isEmpty():
                print("Stack is empty.")
            else:
                print("Popped:", s.pop())

        elif choice == "3":
            if s.isEmpty():
                print("Stack is empty.")
            else:
                print("Top:", s.top())

        elif choice == "4":
            print("isEmpty:", s.isEmpty())

        elif choice == "5":
            print("Size:", s.getCount())

        elif choice == "6":
            print("Stack:", s)

        elif choice == "7":
            running = False

        else:
            print("Invalid choice, please try again.")


def test_queue():
    print("\nChoose queue type:")
    print("1. Shuffling Queue")
    print("2. Circular Queue")
    type_choice = input("Enter choice: ")

    if type_choice == "1":
        q = DSAShufflingQueue(20)
        print("\n--- Testing DSAShufflingQueue ---")
    else:
        q = DSACircularQueue(20)
        print("\n--- Testing DSACircularQueue ---")

    running = True
    while running:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. isEmpty")
        print("4. isFull")
        print("5. Size (count)")
        print("6. Display queue")
        print("7. Back to main menu")
        choice = input("Enter choice: ")

        if choice == "1":
            if q.isFull():
                print("Queue is full.")
            else:
                value = get_enqueue_number()
                q.enqueue(value)
                print("Enqueued", value)

        elif choice == "2":
            if q.isEmpty():
                print("Queue is empty.")
            else:
                print("Dequeued:", q.dequeue())

        elif choice == "3":
            print("isEmpty:", q.isEmpty())

        elif choice == "4":
            print("isFull:", q.isFull())

        elif choice == "5":
            print("Size:", q.getCount())

        elif choice == "6":
            print("Queue:", q)

        elif choice == "7":
            running = False

        else:
            print("Invalid choice, please try again.")


def test_equation_solver():
    print("\n--- Testing EquationSolver ---")
    solver = EquationSolver()
    running = True

    while running:
        equation = input("Enter an equation (e.g. ( 3 + 4 ) * 2), or 'back' to return: ")
        if equation == "back":
            running = False
        else:
            result = solver.solve(equation)
            print(equation, "=", result)


def main():
    running = True
    while running:
        print("\n=== Test Menu ===")
        print("1. Test Stack")
        print("2. Test Queue")
        print("3. Test Equation Solver")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            test_stack()
        elif choice == "2":
            test_queue()
        elif choice == "3":
            test_equation_solver()
        elif choice == "4":
            running = False
        else:
            print("Invalid choice, please try again.")

    print("Exiting.")


main()