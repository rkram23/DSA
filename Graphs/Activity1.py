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

    def insertSorted(self, data, keyLabel):
        newNode = DSAListNode(data)
        current = self.head
        previous = None
        positioned = False
        duplicate = False
        while current is not None and positioned == False:
            if current.data.label == keyLabel:
                duplicate = True
                positioned = True
            elif current.data.label > keyLabel:
                positioned = True
            else:
                previous = current
                current = current.next
        if duplicate == False:
            if previous is None:
                newNode.next = self.head
                self.head = newNode
                if self.tail is None:
                    self.tail = newNode
            else:
                newNode.next = current
                previous.next = newNode
                if current is None:
                    self.tail = newNode

    def removeByLabel(self, label):
        current = self.head
        previous = None
        removed = False
        while current is not None and removed == False:
            if current.data.label == label:
                removed = True
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current is self.tail:
                    self.tail = previous
            else:
                previous = current
                current = current.next
        return removed

class DSAGraphVertex:
    def __init__(self, inLabel, inValue=None):
        self.label = inLabel
        self.value = inValue
        self.links = DSALinkedList()   
        self.visited = False

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited

    def degree(self):
        current = self.links.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def hasLinkTo(self, label):
        current = self.links.head
        found = False
        while current is not None and found == False:
            if current.data.label == label:
                found = True
            else:
                current = current.next
        return found

    def addLink(self, otherVertex):
        if self.hasLinkTo(otherVertex.label) == False:
            self.links.insertSorted(otherVertex, otherVertex.label)

    def removeLink(self, label):
        return self.links.removeByLabel(label)

    def getAdjacent(self):
        result = DSALinkedList()
        current = self.links.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def toString(self):
        return self.label

class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()   
        self.vertexCount = 0
        self.edgeCount = 0

    def hasVertex(self, label):
        current = self.vertices.head
        found = False
        while current is not None and found == False:
            if current.data.label == label:
                found = True
            else:
                current = current.next
        return found

    def getVertex(self, label):
        current = self.vertices.head
        result = None
        while current is not None and result is None:
            if current.data.label == label:
                result = current.data
            current = current.next
        return result

    def addVertex(self, label, value=None):
        if self.hasVertex(label) == False:
            newVertex = DSAGraphVertex(label, value)
            self.vertices.insertSorted(newVertex, label)
            self.vertexCount = self.vertexCount + 1

    def deleteVertex(self, label):
        if self.hasVertex(label) == True:
            other = self.vertices.head
            while other is not None:
                if other.data.label != label:
                    otherRemoved = other.data.removeLink(label)
                    if otherRemoved == True:
                        self.edgeCount = self.edgeCount - 1
                other = other.next
            self.vertices.removeByLabel(label)
            self.vertexCount = self.vertexCount - 1

    def getVertexCount(self):
        return self.vertexCount

    def addEdge(self, label1, label2, directed=False):
        if self.hasVertex(label1) == False:
            self.addVertex(label1)
        if self.hasVertex(label2) == False:
            self.addVertex(label2)
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)
        if vertex1.hasLinkTo(label2) == False:
            vertex1.addLink(vertex2)
            self.edgeCount = self.edgeCount + 1
            if directed == False:
                vertex2.addLink(vertex1)

    def deleteEdge(self, label1, label2, directed=False):
        if self.hasVertex(label1) == True and self.hasVertex(label2) == True:
            vertex1 = self.getVertex(label1)
            vertex2 = self.getVertex(label2)
            removed = vertex1.removeLink(label2)
            if removed == True:
                self.edgeCount = self.edgeCount - 1
                if directed == False:
                    vertex2.removeLink(label1)

    def getEdgeCount(self):
        return self.edgeCount

    def isAdjacent(self, label1, label2):
        result = False
        if self.hasVertex(label1) == True:
            vertex1 = self.getVertex(label1)
            result = vertex1.hasLinkTo(label2)
        return result

    def getAdjacent(self, label):
        result = None
        if self.hasVertex(label) == True:
            vertex = self.getVertex(label)
            result = vertex.getAdjacent()
        return result

    def displayAsList(self):
        current = self.vertices.head
        while current is not None:
            outputLine = current.data.label + " : "
            neighbour = current.data.links.head
            while neighbour is not None:
                outputLine = outputLine + neighbour.data.label + " "
                neighbour = neighbour.next
            print(outputLine)
            current = current.next

    def displayAsMatrix(self):
        header = "     "
        top = self.vertices.head
        while top is not None:
            header = header + top.data.label + " "
            top = top.next
        print(header)

        row = self.vertices.head
        while row is not None:
            line = row.data.label + " :  "
            col = self.vertices.head
            while col is not None:
                if row.data.hasLinkTo(col.data.label) == True:
                    line = line + "1 "
                else:
                    line = line + "0 "
                col = col.next
            print(line)
            row = row.next


def loadSampleGraph():
    graph = DSAGraph()
    graph.addEdge("A", "B")
    graph.addEdge("A", "C")
    graph.addEdge("A", "D")
    graph.addEdge("B", "E")
    graph.addEdge("C", "D")
    graph.addEdge("D", "F")
    graph.addEdge("E", "F")
    graph.addEdge("F", "G")
    return graph


if __name__ == "__main__":
    testGraph = loadSampleGraph()
    print("--- Adjacency List ---")
    testGraph.displayAsList()
    print("")
    print("--- Adjacency Matrix ---")
    testGraph.displayAsMatrix()
    print("")
    print("Vertices:", testGraph.getVertexCount(), "Edges:", testGraph.getEdgeCount())