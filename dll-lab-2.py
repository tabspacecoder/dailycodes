class node:
    def __init__(self, data):
        self.element = data
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.sz = 0

    def insertLast(self, u):
        # @start-editable@

        newNode = node(u)
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

        newNode = node(u)
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

    def findNode(self, u):
        # @start-editable@

        temp = self.head
        while (temp.next != None):
            if (temp.element == u):
                return temp
            temp = temp.next
        return None
        # @end-editable@

    def insertAfter(self, u, v):
        # @start-editable@

        present = self.findNode(v)
        newNode = node(u)
        if (present == None):
            print("Node not found")
            return
        elif present == self.tail:
            present.next = newNode
            newNode.prev = present
            self.tail = newNode
            self.sz += 1
            return
        else:
            temp = present
            nextNode = temp.next
            temp.next = newNode
            newNode.prev = temp
            newNode.next = nextNode
            nextNode.prev = newNode
            self.sz += 1
            return
        # @end-editable@

    def insertBefore(self, u, v):
        # @start-editable@

        newNode = node(u)
        present = self.findNode(v)
        if (present == None):
            print("Node not found")
            return
        elif present == self.head:
            present.prev = newNode
            newNode.next = present
            self.head = newNode
            self.sz += 1
            return
        else:
            temp = present
            prevNode = temp.prev
            temp.prev = newNode
            newNode.next = temp
            newNode.prev = prevNode
            prevNode.next = newNode
            self.sz += 1
            return
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
            return
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
            return
        # @end-editable@

    def deleteAfter(self, u):
        # @start-editable@

        present = self.findNode(u)
        if (present == None):
            print("Node not found")
            return
        else:
            temp = present
            if (temp == self.tail):
                print("Node not found")
                return
            elif temp == self.tail.prev:
                toDelNode = temp.next
                temp.next = None
                toDelNode.prev = None
                self.tail = temp
                self.sz -= 1
                return
            else:
                toDelNode = temp.next
                temp.next = toDelNode.next
                toDelNode.next.prev = temp
                self.sz -= 1
                return
        # @end-editable@

    def deleteBefore(self, u):
        # @start-editable@

        present = self.findNode(u)
        if (present == None):
            print("Node not found")
            return
        else:
            temp = present
            if (temp == self.head):
                print("Node not found")
                return
            elif temp == self.head.next:
                toDelNode = temp.prev
                toDelNode.next = None
                temp.prev = None
                self.head = temp
                return
            else:
                toDelNode = temp.prev
                temp.prev = toDelNode.prev
                toDelNode.prev.next = temp
                self.sz -= 1
                return
        # @end-editable@

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz == 0

    def printList(self):
        if (self.isEmpty()):
            print("Linked List Empty Exception")
        else:
            count = 0
            tnode = self.head
            while tnode != None:
                count = count + 1
                print(tnode.element, end=" ")
                tnode = tnode.next
                if (tnode == self.head):
                    break
                if (count > self.size()):
                    break
            print(" ")
            tnode = self.tail
            count = 0
            while tnode != None:
                count = count + 1
                print(tnode.element, end=" ")
                tnode = tnode.prev
                if (tnode == self.tail):
                    break
                if (count > self.size()):
                    break
            print(" ")
        return

    # swap the nodes containing u and v
    def swap(self, u, v):
        # @start-editable@

        findU = self.findNode(u)
        findV = self.findNode(v)
        if (findU == None and findV == None):
            print("Node not Found")
            return
        elif findU == None or findV == None:
            print("Node not Found")
            return
        elif (findU == self.tail and findV == self.head) or (findV == self.tail and findU == self.head):
            if (findU == self.tail and findV == self.head):
                Uprev = findU.prev
                Vnext = findV.next
                Uprev.next = findV
                Vnext.prev = findU
                findV.next = None
                findV.prev = Uprev
                findU.prev = None
                findU.next = Vnext
                self.tail = findV
                self.head = findU
                return
            elif (findV == self.tail and findU == self.head):
                Vprev = findV.prev
                Unext = findU.next
                Vprev.next = findU
                Unext.prev = findV
                findU.next = None
                findU.prev = Vprev
                findV.prev = None
                findV.next = Unext
                self.tail = findU
                self.head = findV
                return
        elif findU == self.head or findU == self.tail:
            if findU == self.head:
                Unext = findU.next
                Vprev = findV.prev
                Vnext = findV.next
                Unext.prev = findV
                findV.next = Unext
                Vprev.next = findU
                Vnext.prev = findU
                findU.next = Vnext
                findU.prev = Vprev
                findV.prev = None
                self.head = findV
                return
            else:
                Uprev = findU.prev
                Vprev = findV.prev
                Vnext = findV.next
                Uprev.next = findV
                findV.prev = Uprev
                Vprev.next = findU
                Vnext.prev = findU
                findU.next = Vnext
                findU.prev = Vprev
                findV.next = None
                self.tail = findV
                return
        elif findV == self.head or findV == self.tail:
            if findV == self.head:
                Vnext = findV.next
                Uprev = findU.prev
                Unext = findU.next
                Vnext.prev = findU
                findU.next = Vnext
                Uprev.next = findV
                Unext.prev = findV
                findV.next = Unext
                findV.prev = Uprev
                findU.prev = None
                self.head = findU
                return
            else:
                Vprev = findV.prev
                Uprev = findU.prev
                Unext = findU.next
                Vprev.next = findU
                findU.prev = Vprev
                Uprev.next = findV
                Unext.prev = findV
                findV.next = Unext
                findV.prev = Uprev
                findU.next = None
                self.tail = findU
                return
        else:
            Upos = findU
            Vpos = findV
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
            return
    # @end-editable@


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
        elif (operation[0] == 'FIND'):
            key = dll.findNode(int(operation[1]))
            if (key != None):
                print(key.element)
            else:
                print("Data not Found")
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
        elif (operation[0] == 'SW'):
            dll.swap(int(operation[1]), int(operation[2]))
            dll.printList()
        """elif(operation[0]=="F"):
            print(dll.getHead())
        elif(operation[0]=='L'):
            print(dll.getLastNode())
        """
        inputs -= 1


def main():
    testDLL()


if __name__ == '__main__':
    main()