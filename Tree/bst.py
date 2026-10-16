class DSAListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = DSAListNode(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


class DSATreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DSABinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            self.count += 1
            return DSATreeNode(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def find(self, data):
        return self._find(self.root, data)

    def _find(self, node, data):
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self._find(node.left, data)
        else:
            return self._find(node.right, data)

    def delete(self, data):
        if self._find(self.root, data) is None:
            return False
        self.root = self._delete(self.root, data)
        return True

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # no children
            if node.left is None and node.right is None:
                self.count -= 1
                return None
            # one child
            if node.left is None:
                self.count -= 1
                return node.right
            if node.right is None:
                self.count -= 1
                return node.left
            # two children - replace with inorder successor
            successor = self._find_min(node.right)
            node.data = successor.data
            node.right = self._delete(node.right, successor.data)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def min(self):
        if self.root is None:
            return None
        return self._find_min(self.root).data

    def max(self):
        if self.root is None:
            return None
        return self._find_max(self.root).data

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1  
        left_h = self._height(node.left)
        right_h = self._height(node.right)
        return 1 + (left_h if left_h > right_h else right_h)

    def balance(self):
        if self.root is None:
            return 100.0

        total_imbalance = self._sum_imbalance(self.root)
        node_count = self._count_nodes(self.root)

        if node_count == 0:
            return 100.0

        avg_imbalance = total_imbalance / node_count
        max_possible = self.height() if self.height() > 0 else 1
        score = 100.0 - (avg_imbalance / max_possible) * 100.0

        if score < 0:
            score = 0.0
        return round(score, 2)

    def _sum_imbalance(self, node):
        if node is None:
            return 0
        left_h = self._height(node.left)
        right_h = self._height(node.right)
        imbalance = abs(left_h - right_h)
        return imbalance + self._sum_imbalance(node.left) + self._sum_imbalance(node.right)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def inorder(self):
        result = DSALinkedList()
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

    def preorder(self):
        result = DSALinkedList()
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is not None:
            result.append(node.data)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = DSALinkedList()
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is not None:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.data)


def print_traversal(values):
    line = ""
    curNode = values.head
    first = True
    while curNode is not None:
        if first:
            line = str(curNode.data)
            first = False
        else:
            line = line + ", " + str(curNode.data)
        curNode = curNode.next
    print("[" + line + "]")
