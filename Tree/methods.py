
from bst import DSABinarySearchTree

if __name__ == "__main__":
    tree = DSABinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        tree.insert(v)

    print("Inserted:", values)
    print("Min:", tree.min())
    print("Max:", tree.max())
    print("Height:", tree.height())
    print("Balance score:", tree.balance(), "%")

    # Make it unbalanced
    for v in [90, 100, 110, 120]:
        tree.insert(v)

    print("\nAfter adding 90, 100, 110, 120 (skewed right):")
    print("Height:", tree.height())
    print("Balance score:", tree.balance(), "%")
