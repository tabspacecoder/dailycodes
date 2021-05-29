# Code developed by Ms. Vidhya. S as part of 19CSE212 - Data Structures Course

class node:
    def __init__(self, c=None, e=None, next=None):
        self.coeff = c
        self.exp = e
        self.next = next


class SLList:
    def __init__(self):
        self.head = None
        self.sz = 0

    def insert(self, c, e):
        # @start-editable@

        newNode = node(c, e)
        if self.head == None:
            self.head = newNode
            self.sz += 1
        else:
            temp = self.head
            while temp.next != None:
                if temp.exp == e:
                    temp.coeff = temp.coeff+c
                    return
                temp = temp.next
            temp = self.head
            if e > temp.exp:
                newNode.next = temp
                self.head = newNode
                self.sz += 1
                return
            else:
                while (temp.next != None and e < temp.next.exp):
                    temp = temp.next
                newNode.next = temp.next
                temp.next = newNode
                self.sz += 1
                return

        # @end-editable@

    def printList(self):
        tnode = self.head
        while tnode != None:
            if (tnode != self.head):
                print(" + ", end="")
            if (tnode.exp == 0):
                str1 = str(tnode.coeff)
            else:
                str1 = str(tnode.coeff) + "x^" + str(tnode.exp)
            print(str1, end="")
            tnode = tnode.next
        print("")
        return

    def findNode(self, val):
        curnode = self.head
        while curnode != None:
            if curnode.element == val:
                return curnode
            curnode = curnode.next
        return None

    def isEmpty(self):
        return self.sz == 0

    def size(self):
        return self.sz


def readPolynomial():
    poly = SLList()
    while (1):
        # print("Coeff")
        coeff = int(input())
        # print("exp")
        exp = int(input())
        poly.insert(coeff, exp)
        # print("choice")
        choice = input()
        if (choice == "y"):
            break
    return poly


def addPolynomial(p1, p2):
    # @start-editable@

    fin = SLList()
    t1 = p1.head
    t2 = p2.head
    while t1 != None :
        fin.insert(t1.coeff, t1.exp)
        t1 = t1.next

    while t2!=None:
        fin.insert(t2.coeff, t2.exp)
        t2 = t2.next
    return fin
    # @end-editable@


def testSLL():
    inputs = int(input())
    while inputs > 0:
        p1 = readPolynomial()
        p1.printList()
        p2 = readPolynomial()
        p2.printList()
        r = addPolynomial(p1, p2)
        r.printList()
        inputs -= 1


def main():
    testSLL()


if __name__ == '__main__':
    main()