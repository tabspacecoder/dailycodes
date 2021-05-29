import math

#filled by Mugunth J C - CB.EN.U4CSE19440
class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0

    def findElement(self, e):
        temp=self.root
        if e < temp.element:
            if temp.leftchild == None:
                return None
            return temp.leftchild.findElement(e)
        elif e > temp.element:
            if temp.rightchild == None:
                return None
            return temp.rightchild.findElement(e)
        else:
            return temp

    def addLeft(self, e,parent):
        parent.leftchild = e
        self.sz = self.sz + 1
        return

    def addRight(self, e,parent):
        parent.rightchild = e
        self.sz = self.sz + 1
        return

    def getChildren(self, curnode):
        children = []
        children.append(curnode.leftchild)
        children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if curnode.rightchild==None and curnode.leftchild==None:
            return 1
        else:
            return 0

    def inorderTraverse(self, v):
        return

    def preorderTraverse(self, v):
        return

    def postorderTraverse(self, v):
        return

    def findDepth(self, v):
        if v.parent is not None:
            return 1 + self.findDepth(v.parent)
        else:
            return 0

    def findHeight(self, v):
        if self.isEmpty()==0:
            return self.isEmpty()
        else:
            return 1 + max(self.findHeight(v.leftchild), self.findHeight(v.rightchild))

    def deleteNode(self, n):
        if n != None:
            if n.parent != None:
                if n.parent.leftchild == n:
                    n.parent.leftchild = None
                    if n.leftchild != None:
                        n.leftchild.parent=n.parent
                    if n.rightchild!= None:
                        n.rightchild.parent=n.parent
                elif n.parent.rightchild == n:
                    n.parent.rightchild = None
                    if n.leftchild != None:
                        n.leftchild.parent=n.parent
                    if n.rightchild!= None:
                        n.rightchild.parent=n.parent

    def sibling(self, v):
        if v == v.parent.rightchild:
            return v.parent.leftchild
        else:
            return v.parent.rightchild

    def isRoot(self, v):
        if v.parent == None:
            return 1
        else:
            return 0

    def buildTree(self, eltlist):
        nodelist = [None]
        for i in range(len(eltlist)):
            if i != 0:
                if eltlist[i] is not None:
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[math.floor(i / 2)]
                        if i % 2 == 0:
                            nodelist[math.floor(i / 2)].leftchild = tempnode
                        else:
                            nodelist[math.floor(i / 2)].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)
        self.root = nodelist[1]
        # print "final nodelist", len(nodelist)
        return nodelist

    def isEmpty(self):
        if self.sz == 0:
            return 1
        else:
            return 0

    def size(self):
        return self.sz


def main():
    tree = BinaryTree()
    print(tree.size())
    A = []
    A = [None, 1, 2, 3, 4, 17, 5, 12, 7, 8, None, 9, None, None, None, None, None, None, None, None, None, None, 10]
    nlist = tree.buildTree(A)
    print("Inorder Traversal:")
    tree.inorderTraverse(tree.root)
    print("Preorder Traversal:")
    tree.preorderTraverse(tree.root)
    print("Postorder Traversal:")
    tree.postorderTraverse(tree.root)
    print("Height of the Tree:")
    print(tree.findHeight(tree.root))
    print("Depth of the Tree:")
    print(tree.findDepth(tree.root))


if __name__ == '__main__':
    main()
