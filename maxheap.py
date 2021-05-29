class BinHeap():
    def _init_(self):
        self.heapList = [0]
        self.currentSize = 0

    """ This method defines the upheap function when inserting an element
    """

    def upHeapp(self, i):

        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        # @start-editable@

        self.currentSize += 1
        self.heapList.append(k)
        self.upHeapp(self.currentSize)

        # @end-editable@
        self.printHeap()

    """ This method defines the downheap function when removing min
    """

    def downHeap(self, i):
        # @start-editable@

        while (2 * i <= self.currentSize):
            ind = self.maxChild(i)
            if (self.heapList[ind] > self.heapList[i]):
                self.heapList[ind], self.heapList[i] = self.heapList[i], self.heapList[ind]
            i = ind

        # @end-editable@
        '''  
        maxChils retrurns the location of the largest child of the current location
        '''

    def maxChild(self, i):
        # @start-editable@

        if (i * 2 + 1 > self.currentSize):
            return None
        if (i * 2 + 1 > self.currentSize):
            return i * 2
        if (self.heapList[i * 2] > self.heapList[i * 2 + 1]):
            return i * 2
        else:
            return i * 2 + 1

        # @end-editable@

    def deleteop(self):

        if len(self.heapList) == 1:
            return 'Empty heap'
        root = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop(self.currentSize)
        self.currentSize -= 1
        self.downHeap(1)
        self.printHeap()
        return root

    def buildHeap(self, alist):
        # @start-editable@

        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.downHeap(i)
            i = i - 1

        # @end-editable@
        self.printHeap()

    def printHeap(self):
        print(self.heapList)

    def klargest(self, k):
        # @start-editable@

        for i in range(1, k):
            self.deleteop()

        # @end-editable@
        return self.heapList[1]


def main():
    heap = BinHeap()
    arraysize = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    heap.buildHeap(arr)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "I"):
            heap.insert(int(operation[1]))

        elif (operation[0] == "D"):
            heap.deleteop()

        elif (operation[0] == "K"):
            kthlargest = heap.klargest(k)
            print(kthlargest)

        inputs -= 1


if __name__ == '__main__':
    main()