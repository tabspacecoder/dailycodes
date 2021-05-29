"""The code is borrowed from the book "Problem Solving with Algorithms and Data Structures"
   http://interactivepython.org/OiXhZ/courselib/static/pythonds/SortSearch/Hashing.html

"""


class HashTable:
    # This implementation uses two lists. One list, called slots, will hold the key items and a parallel list, called data, will hold the data values. When we look up a key, the corresponding position in the data list will hold the associated data value.
    def __init__(self, size, resolutionMethod):
        self.size = int(size)
        self.slots = [None] * self.size
        self.resolutionMethod = resolutionMethod

    def print(self):
        print(self.slots)

    ## inserts the key, data pair into the table using hashing
    def insert(self, data):
        # @start-editable@

        self.hashfunction(data, self.size)
        # @end-editable@

    def collisionResolutionStrategies(self, oldhash, size, j, key):
        if self.resolutionMethod == 1:
            return self.linearProbing(oldhash, size, j)
        elif self.resolutionMethod == 2:
            return self.quadraticProbing(oldhash, size, j)
        elif self.resolutionMethod == 3:
            return self.doubleHashing(oldhash, size, j, key)

    def hashfunction(self, key, size):
        # @start-editable@

        h = key % size
        if self.slots[h] is not None:
            self.collisionResolutionStrategies(h, size, key, 0)
        else:
            self.slots[h] = key
            # @end-editable@

    ## this gives the position using linear probing
    def linearProbing(self, oldhash, size, j):
        # @start-editable@

        for i in range(1, size):
            k = (j + i) % size
            if self.slots[k] is None:
                self.slots[k] = j
                return
        # @end-editable@

    def quadraticProbing(self, oldhash, size, j):
        # @start-editable@

        for i in range(1, size):
            k = (j + i * i) % size
            if self.slots[k] is None:
                self.slots[k] = j
                return
        # @end-editable@

    def doubleHashing(self, oldhash, size, j, key):
        # @start-editable@

        def GetPrime():
            for i in range(size, 1, -1):
                Stat = True
                for j in range(2, i):
                    if i % j == 0:
                        Stat = False
                        break
                if Stat:
                    return i
            return -1

        Prime = GetPrime()
        hash1 = oldhash
        hash2 = Prime - (j % Prime)
        for i in range(size):
            hash = (hash1 + i * hash2) % size
            if self.slots[hash] is None:
                self.slots[hash] = j
                return
                # @end-editable@

    ## retrieves the item from the table based on the hashing. Print the starting slot for searching the key, Returns True when key is found and False when the key is not found"
    def search(self, data):
        # @start-editable@

        for i in range(self.size):
            if data == self.slots[i]:
                print("start slot ", data % self.size)
                return "True"
        print("start slot ", data % self.size)
        return "False"
        # @end-editable@

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def testHash():
    collisionResolutionMethod = int(input())
    hashtablesize = int(input())
    H = HashTable(hashtablesize, collisionResolutionMethod)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "I"):
            H.insert(int(operation[1]))
        elif (operation[0] == "S"):
            print(H.search(int(operation[1])))
        elif (operation[0] == "P"):
            H.print()
        inputs -= 1


def main():
    testHash()


if __name__ == '__main__':
    main()