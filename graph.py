"""The code is borrowed from the book "Problem Solving with Algorithms and Data Structures"
   http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html

"""
from collections import OrderedDict


class BinHeap():
    def _init_(self):
        self.heapList = [0]
        self.currentSize = 0

    """ This method defines the upheap function when inserting an element
    """

    def upHeapp(self, i):

        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.upHeapp(self.currentSize)

    def size(self):
        return self.currentSize

    """ This method defines the downheap function when removing min
    """

    def downHeap(self, i):
        while (i * 2) <= self.currentSize:
            min = self.minChild(i)
            if self.heapList[i] > self.heapList[min]:
                self.heapList[i], self.heapList[min] = self.heapList[min], self.heapList[i]
            i = min

    def minChild(self, i):
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1

    def delMin(self):
        if len(self.heapList) == 1:
            return 'Empty heap'
        root = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop(self.currentSize)
        self.currentSize -= 1
        self.downHeap(1)
        # self.printHeap()
        return root

    # create a method to print the contents of the heap in level order
    def printHeap(self):
        print(self.heapList)

    '''
    Graph ADT starts from here
    '''


class Vertex:
    def _init_(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def _str_(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def _init_(self):
        self.vertList = {}
        self.numVertices = 0
        self.front = []
        self.back = []
        self.depfs = []

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.vertList = OrderedDict(sorted(self.vertList.items()))
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def _contains_(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):  # f is from node, t is to node
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def _iter_(self):
        return iter(self.vertList.values())

    """
    Write a method to generate an adjacency matrix representation of the graph
    """

    def createAdjMatrix(self):
        adjmat = list()
        # @start-editable@

        for x in sorted(self.vertList):
            key = self.vertList[x]
            temp = []
            for y in sorted(self.vertList):
                anotherkey = self.vertList[y]
                if anotherkey in key.connectedTo:
                    temp.append(key.connectedTo[anotherkey])
                else:
                    temp.append(0)
            adjmat.append(temp)

        # @end-editable@
        print("Adjacency matrix")
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print(adjmat[i][j], end=" ")
            print("")
        return

    def printdfs(self):
        print("Front edges:", self.front)
        print("Back edges:", self.back)
        print("dfs:", self.depfs)

    """
    Write a method to traverse the graph using dfs from start node. 
    The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or backward edge.
    """

    def dfs(self, stnode):
        self.depfs.append(stnode.getId())
        neighbours = list(stnode.getConnections())

        # @start-editable@

        self.depfs = []
        visited = {}
        visited[stnode.getId()] = True
        self.time = 0
        pre = {}
        post = {}
        triedge = []
        cross = []

        def recur(x):
            self.depfs.append(x.getId())
            pre[x.getId()] = self.time
            self.time += 1
            for i in self.vertList[x.getId()].connectedTo:
                if i.getId() in visited:
                    self.back.append([x.getId(), i.getId()])
                else:
                    self.front.append([x.getId(), i.getId()])
                    visited[i.getId()] = True
                    recur(i)

            post[x.getId()] = self.time
            self.time += 1

        recur(stnode)

        # @end-editable@
        return

    """
    Write a method to traverse the graph using bfs from start node.  The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or cross edge.
    """

    def bfs(self, stnode):
        queue = []
        breadth = []
        cross = []
        breadth.append(stnode.getId())
        queue.append(stnode.getId())

        # @start-editable@

        breadth = []
        visited = {}
        visited[stnode.getId()] = True
        while (len(queue) > 0):
            temp = queue[0]
            queue.pop(0)
            breadth.append(temp)
            for x in self.vertList[temp].connectedTo:
                if x.getId() in visited:
                    cross.append([temp, x.getId()])
                else:
                    queue.append(x.getId())
                    visited[x.getId()] = True

        # @end-editable@
        print("Bfs:", breadth)
        print("Cross edge:", cross)
        return

    """
    Write a method to generate the minimum spanning tree of the graph using Kruskal algorithm
    """

    def mstKruskal(self):
        wt = BinHeap()
        edge = {}
        tree = []
        re = []

        # @start-editable@

        ed = []
        for k in self.vertList:
            for i in self.vertList[k].connectedTo:
                tmp = [k, i.getId(), self.vertList[k].connectedTo[i]]
                ed.append(tmp)
        sed = []
        sed = sorted(ed, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(0, 11):
            parent.append(node)
            rank.append(0)
        it = 0
        e = 0

        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        while e < 10:

            u, v, w = sed[it]
            it = it + 1
            x = find(parent, u)
            y = find(parent, v)

            if x != y:
                e = e + 1
                re.append([u, v])
                union(parent, rank, x, y)

                # @end-editable@
        print("Minimum spanning tree:", sorted(re))
        return


def testGraph():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList
    g.addEdge(5, 1, 8)
    g.addEdge(1, 2, 19)
    g.addEdge(5, 0, 10)
    g.addEdge(4, 6, 11)
    g.addEdge(6, 10, 23)
    g.addEdge(10, 9, 33)
    g.addEdge(9, 8, 7)
    g.addEdge(6, 7, 6)
    g.addEdge(8, 7, 1)
    g.addEdge(9, 6, 9)
    g.addEdge(7, 10, 14)
    g.addEdge(0, 4, 15)
    g.addEdge(0, 3, 16)
    g.addEdge(0, 2, 5)
    g.addEdge(0, 1, 2)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 30)
    g.addEdge(4, 5, 18)
    g.addEdge(5, 2, 22)
    g.addEdge(3, 1, 17)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "A"):
            AdjMat = g.createAdjMatrix()
        elif (operation[0] == "B"):
            start = g.getVertex(int(operation[1]))
            g.bfs(start)
        elif (operation[0] == "D"):
            start = g.getVertex(int(operation[1]))
            g.dfs(start)
            g.printdfs()
        elif (operation[0] == "M"):
            g.mstKruskal()
        inputs -= 1


def main():
    testGraph()


if _name_ == '_main_':
    main()