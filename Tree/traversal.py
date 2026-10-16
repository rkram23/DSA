from bst import DSABinarySearchTree, print_traversal

if __name__ == "__main__":
    tree = DSABinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        tree.insert(v)

    print("Inserted:", values)
    print("Inorder:  ", end="")
    print_traversal(tree.inorder())
    print("Preorder: ", end="")
    print_traversal(tree.preorder())
    print("Postorder:", end="")
    print_traversal(tree.postorder())
