from bst import DSABinarySearchTree, print_traversal


def menu():
    tree = DSABinarySearchTree()

    while True:
        print("\n--- Binary Search Tree Menu ---")
        print("1. Add node")
        print("2. Delete node")
        print("3. Display tree (inorder / preorder / postorder)")
        print("4. Min / Max / Height")
        print("5. Balance score")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                value = int(input("Enter value to add: ").strip())
                tree.insert(value)
                print(f"{value} added.")
            except ValueError:
                print("Invalid number.")

        elif choice == "2":
            try:
                value = int(input("Enter value to delete: ").strip())
                if tree.delete(value):
                    print(f"{value} deleted.")
                else:
                    print(f"{value} not found in tree.")
            except ValueError:
                print("Invalid number.")

        elif choice == "3":
            if tree.root is None:
                print("Tree is empty.")
                continue
            order = input("Traversal (in/pre/post): ").strip().lower()
            if order == "in":
                print_traversal(tree.inorder())
            elif order == "pre":
                print_traversal(tree.preorder())
            elif order == "post":
                print_traversal(tree.postorder())
            else:
                print("Invalid traversal type.")

        elif choice == "4":
            if tree.root is None:
                print("Tree is empty.")
                continue
            print(f"Min: {tree.min()}")
            print(f"Max: {tree.max()}")
            print(f"Height: {tree.height()}")

        elif choice == "5":
            print(f"Balance score: {tree.balance()}%")

        elif choice == "6":
            print("Exiting.")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
