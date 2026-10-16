from Activity1 import DSAListNode, DSAGraphVertex, DSAGraph, loadSampleGraph

class DSAQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        result = False
        if self.front is None:
            result = True
        return result

    def enqueue(self, value):
        newNode = DSAListNode(value)
        if self.rear is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.count = self.count + 1

    def dequeue(self):
        result = None
        if self.front is not None:
            result = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.count = self.count - 1
        return result

    def getCount(self):
        return self.count


class DSAStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def isEmpty(self):
        result = False
        if self.top is None:
            result = True
        return result

    def push(self, value):
        newNode = DSAListNode(value)
        newNode.next = self.top
        self.top = newNode
        self.count = self.count + 1

    def pop(self):
        result = None
        if self.top is not None:
            result = self.top.data
            self.top = self.top.next
            self.count = self.count - 1
        return result

    def peek(self):
        result = None
        if self.top is not None:
            result = self.top.data
        return result


def nextUnvisited(self):
    current = self.links.head
    result = None
    while current is not None and result is None:
        if current.data.getVisited() == False:
            result = current.data
        current = current.next
    return result


DSAGraphVertex.nextUnvisited = nextUnvisited


def clearAllVisited(self):
    current = self.vertices.head
    while current is not None:
        current.data.clearVisited()
        current = current.next


def getStartVertex(self, startLabel):
    if self.hasVertex(startLabel) == True:
        result = self.getVertex(startLabel)
    else:
        result = self.vertices.head.data
    return result


DSAGraph.clearAllVisited = clearAllVisited
DSAGraph.getStartVertex = getStartVertex



def breadthFirstSearch(self, startLabel):
    T = DSAQueue()
    Q = DSAQueue()
    self.clearAllVisited()

    v = self.getStartVertex(startLabel)
    v.setVisited()
    Q.enqueue(v)

    while Q.isEmpty() == False:
        v = Q.dequeue()
        w = v.links.head
        while w is not None:
            if w.data.getVisited() == False:
                T.enqueue(v)
                T.enqueue(w.data)
                w.data.setVisited()
                Q.enqueue(w.data)
            w = w.next
    return T


DSAGraph.breadthFirstSearch = breadthFirstSearch

def depthFirstSearch(self, startLabel):
    T = DSAQueue()
    S = DSAStack()
    self.clearAllVisited()

    v = self.getStartVertex(startLabel)
    v.setVisited()
    S.push(v)

    while S.isEmpty() == False:
        w = v.nextUnvisited()
        while w is not None:
            T.enqueue(v)
            T.enqueue(w)
            w.setVisited()
            S.push(w)
            v = w
            w = v.nextUnvisited()
        v = S.pop()
    return T


DSAGraph.depthFirstSearch = depthFirstSearch

def displayTraversal(T):
    if T.isEmpty() == True:
        print("(no edges - graph may have a single vertex, or is empty)")
    else:
        while T.isEmpty() == False:
            fromVertex = T.dequeue()
            toVertex = T.dequeue()
            print(fromVertex.label + " -> " + toVertex.label)

if __name__ == "__main__":
    testGraph = loadSampleGraph()

    print("--- Breadth First Search from A ---")
    bfsResult = testGraph.breadthFirstSearch("A")
    displayTraversal(bfsResult)

    print("")
    print("--- Depth First Search from A ---")
    dfsResult = testGraph.depthFirstSearch("A")
    displayTraversal(dfsResult)