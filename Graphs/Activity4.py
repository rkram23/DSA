from Activity1 import loadSampleGraph
from Activity3 import displayTraversal


def runMenu():
    graph = loadSampleGraph()
    running = True

    while running == True:
        print("")
        print("=== DSA Graph Menu ===")
        print("Vertices: " + str(graph.getVertexCount()) +
              "   Edges: " + str(graph.getEdgeCount()))
        print("a) Add node")
        print("b) Delete node")
        print("c) Add edge")
        print("d) Delete edge")
        print("e) Display as list")
        print("f) Display as matrix")
        print("g) Breadth First Search")
        print("h) Depth First Search")
        print("q) Quit")
        choice = input("Enter option: ")

        if choice == "a":
            label = input("Enter label for new vertex: ")
            graph.addVertex(label)
            print("Vertex " + label + " added.")

        elif choice == "b":
            label = input("Enter label of vertex to delete: ")
            if graph.hasVertex(label) == True:
                graph.deleteVertex(label)
                print("Vertex " + label + " deleted.")
            else:
                print("No such vertex: " + label)

        elif choice == "c":
            label1 = input("Enter first vertex label: ")
            label2 = input("Enter second vertex label: ")
            graph.addEdge(label1, label2)
            print("Edge " + label1 + " - " + label2 + " added.")

        elif choice == "d":
            label1 = input("Enter first vertex label: ")
            label2 = input("Enter second vertex label: ")
            graph.deleteEdge(label1, label2)
            print("Edge " + label1 + " - " + label2 + " removed (if it existed).")

        elif choice == "e":
            print("Adjacency List")
            graph.displayAsList()

        elif choice == "f":
            print("Adjacency Matrix")
            graph.displayAsMatrix()

        elif choice == "g":
            startLabel = input("Enter start vertex label: ")
            if graph.hasVertex(startLabel) == True:
                print("--- Breadth First Search from " + startLabel + " -")
                T = graph.breadthFirstSearch(startLabel)
                displayTraversal(T)
            else:
                print("No such vertex: " + startLabel)

        elif choice == "h":
            startLabel = input("Enter start vertex label: ")
            if graph.hasVertex(startLabel) == True:
                print("Depth First Search from " + startLabel + " -")
                T = graph.depthFirstSearch(startLabel)
                displayTraversal(T)
            else:
                print("No such vertex: " + startLabel)

        elif choice == "q":
            running = False
            print("Goodbye.")

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    runMenu()
