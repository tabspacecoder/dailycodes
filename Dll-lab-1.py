class DLList:
    class node:
        def __init__(self, data):
            self.element = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = self.node(None)
        self.tail = self.head
        self.sz = 0

    def getHead(self):
        # @start-editable@

        if self.sz != 0:
            self.head

        # @end-editable@

    def getLastNode(self):
        # @start-editable@

        if self.sz != 0:
            return self.tail

    # @end-editable@

    def insertLast(self, u):
        # @start-editable@

        newNode = self.node(u)
        if self.sz == 0:
            self.head = newNode
            self.tail = newNode
            self.sz = self.sz + 1
            return

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.sz = self.sz + 1
            return


# @end-editable@


    def insertFirst(self, u):
        # @start-editable@

        newNode = self.node(u)
        if self.sz == 0:
            self.head = newNode
            self.tail = newNode
            self.sz = self.sz + 1
            return

        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.sz = self.sz + 1
            return


# @end-editable@


# insert a node with value u after the node containing value v
# error message: Node to insert after not found
    def insertAfter(self, u, v):
        # @start-editable@

        present = self.findNode(v)
        if (present == 0):
            print("Node to insert after not found")
        else:
            newNode = self.node(u)
            temp = self.head
            while (temp.next != None):
                if (temp.element == v):
                    break
                temp = temp.next
            nextNode = temp.next
            temp.next = newNode
            newNode.prev = temp
            newNode.next = nextNode
            nextNode.prev = newNode
            self.sz += 1


# @end-editable@


# insert a node with value u before the node containing value v
# error message: Node to insert before not found
    def insertBefore(self, u, v):
        # @start-editable@

        present = self.findNode(v)
        if (present == 0):
            print("Node to insert before not found")
        else:
            newNode = self.node(u)
            temp = self.head
            while (temp.next != None):
                if (temp.element == v):
                    break
                temp = temp.next
            prevNode = temp.prev
            temp.prev = newNode
            newNode.next = temp
            newNode.prev = prevNode
            prevNode.next = newNode
            self.sz += 1


# @end-editable@


    def deleteFirst(self):
        # @start-editable@

        if self.sz == 0:
            return
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.sz -= 1


# @end-editable@


    def deleteLast(self):
        # @start-editable@

        if self.sz == 0:
            return
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.sz -= 1


# @end-editable@


# delete the node after the node containting value u
# error message: Node to delete after not found
    def deleteAfter(self, u):
        # @start-editable@

        present = self.findNode(u)
        if (present == 0):
            print("Node to delete after not found")
        else:
            temp = self.head
            while (temp.next != None):
                if (temp.element == u):
                    break
                temp = temp.next
            if (temp == self.tail):
                print("Node to delete after not found")
            else:
                toDelNode = temp.next
                temp.next = toDelNode.next
                toDelNode.next.prev = temp
                self.sz -= 1


# @end-editable@


# delete the node before the node containting value u
# error message: Node to delete before not found
    def deleteBefore(self, u):
        # @start-editable@

        present = self.findNode(u)
        if (present == 0):
            print("Node to delete before not found")
        else:
            temp = self.head
            while (temp.next != None):
                if (temp.element == u):
                    break
                temp = temp.next
            if (temp == self.head):
                print("Node to delete after not found")
            else:
                toDelNode = temp.prev
                temp.prev = toDelNode.prev
                toDelNode.prev.next = temp
                self.sz -= 1


# @end-editable@


    def findNode(self, val):
        # @start-editable@

        flag = 0
        temp = self.head
        while (temp.next != None):
            if (temp.element == val):
                flag = 1
        return flag

    # @end-editable@


# swap the nodes containing u and v
    def swap(self, u, v):
        # @start-editable@

        findU = self.findNode(u)
        findV = self.findNode(v)
        if (findU == 0 and findV == 0):
            return
        else:
            Upos = self.head
            Vpos = self.head
            while (Vpos.next != None):
                if (Vpos.element == v):
                    break
                Vpos = Vpos.next
            while (Upos.next != None):
                if (Upos.element == u):
                    break
                Upos = Upos.next
            tempU = Upos
            tempV = Vpos
            Upos.next.prev = Vpos
            Upos.prev.next = Vpos
            Vpos.next = tempU.next
            Vpos.prev = tempU.Prev
            tempV.next.prev = Upos
            tempV.prev.next = Upos
            Upos.next = tempV.next
            Upos.prev = tempV.prev


# @end-editable@


    def isEmpty(self):
        # @start-editable@

        # @end-editable@
        return (self.sz == 0)


    def size(self):
        # @start-editable@

        # @end-editable@
        return self.sz


    def printList(self):
        if (self.isEmpty()):
            print("Linked List Empty Exception")
        else:
            tnode = self.head
            while tnode != None:
                print(tnode.element, end="->")
                tnode = tnode.next
            print(" ")
            tnode = self.tail
            while tnode != None:
                print(tnode.element, end="->")
                tnode = tnode.prev
            print(" ")
        return


def testDLL():
    dll = DLList()
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "S"):
            print(dll.size())
        elif (operation[0] == "I"):
            print(dll.isEmpty())
        elif (operation[0] == "IF"):
            dll.insertFirst(int(operation[1]))
            dll.printList()
        elif (operation[0] == "IL"):
            dll.insertLast(int(operation[1]))
            dll.printList()
        elif (operation[0] == "DF"):
            dll.deleteFirst()
            dll.printList()
        elif (operation[0] == "DL"):
            dll.deleteLast()
            dll.printList()
        elif (operation[0] == "IA"):
            dll.insertAfter(int(operation[1]), int(operation[2]))
            dll.printList()
        elif (operation[0] == "IB"):
            dll.insertBefore(int(operation[1]), int(operation[2]))
            dll.printList()
        elif (operation[0] == "DA"):
            dll.deleteAfter(int(operation[1]))
            dll.printList()
        elif (operation[0] == "DB"):
            dll.deleteBefore(int(operation[1]))
            dll.printList()
        elif (operation[0] == "F"):
            print(dll.getHead().element)
        elif (operation[0] == 'L'):
            print(dll.getLastNode().element)
        elif (operation[0] == 'FIND'):
            temp = dll.findNode(int(operation[1]))
            if (temp != None):
                print(temp.element)
            else:
                print("NULL")
        elif (operation[0] == 'SW'):
            dll.swap(int(operation[1]), int(operation[2]))
            dll.printList()
        inputs -= 1


def main():
    testDLL()


if __name__ == '__main__':
    main()