class DLList:
    class node:
        def _init_(self,data):
           self.element = data
           self.next = None
           self.prev = None
           
          
    def _init_(self):
        self.head = self.node(None)
        self.tail = self.head
        self.sz = 0
    def getHead(self):
        #@start-editable@
        return self.head
            
            
    #@end-editable@
        return
    
    def getLastNode(self):
        #@start-editable@
        return self.tail
            
            
    #@end-editable@
        return
     
    def insertLast(self,u):
        #@start-editable@
        myNode=self.node(u)
        if(self.sz==0):
          self.tail=myNode
          self.head=myNode
        else:
          self.tail.next=myNode
          temp.prev=self.tail
          self.tail=myNode
        self.sz+=1
            
            
    #@end-editable@
        return
    def insertFirst(self,u):
        #@start-editable@
        myNode=self.node(u)
        if(self.sz==0):
          self.head=myNode
          self.tail=myNode
        else:
          myNode.next=self.head
          self.head.prev=myNode
          self.head=myNode
        self.sz+=1
            
            
    #@end-editable@
        return
        
         
    #insert a node with value u after the node containing value v
    # error message: Node to insert after not found
    def insertAfter(self,u,v):
        #@start-editable@
        temp=self.node(u)
        curnode=self.head
        tnode=self.tail
        f=0
        if(self.sz==0):
          return None
        if(self.sz==1 and tnode.element==v):
          self.insertLast(u)
          f=1
          return
        while(curnode.next!=None):
          if(curnode.element==v):
            temp.next=curnode.next
            temp.prev=curnode
            curnode.next.prev=temp
            curnode.next=temp
            self.sz+=1
            f=1
            break
          curnode=curnode.next
        if(f!=1):
          if(tnode.element==v):
            self.insertLast(u)
            f=1
        if(f==0):
          print("Node to insert after not found")
            
    #@end-editable@
        return

    #insert a node with value u before the node containing value v
    # error message: Node to insert before not found
    def insertBefore(self,u,v):
        #@start-editable@
        temp=self.node(u)
        curnode=self.tail
        tnode=self.head
        f=0
        if(self.sz==0):
          return None
        if(self.sz==1 and tnode.element==v):
          self.insertFirst(u)
          f=1
          return
        if(self.sz==1 and tnode.element!=v):
          return None
        if(tnode.element==v):
          self.insertFirst(u)
          f=1
          return
        while(tnode!=None):
          if(tnode.element==v):
            temp.prev=tnode.prev
            temp.next=tnode
            tnode.prev=temp
            temp.prev.next=temp
            self.sz+=1
            f=1
            break
          tnode=tnode.next
        if(f==0):
          print("Node to insert before not found")
            
    #@end-editable@
        return
    def deleteFirst(self):
        #@start-editable@
        if(self.sz==0):
          return None
        elif(self.sz==1):
          self.tail=None
          self.head=None
          self.sz-=1
        else:
          myNode=self.head.next
          myNode.prev.next=None
          myNode.prev=None
          self.head=myNode
          self.sz-=1
            
    #@end-editable@
        return
    def deleteLast(self):
        #@start-editable@
        if(self.sz==0):
          return None
        elif(self.sz==1):
          self.head=None
          self.tail=None
          self.sz-=1
        else:
          myNode=self.tail.prev
          myNode.next.prev=None
          myNode.next=None
          self.tail=myNode
          self.sz-=1
            
    #@end-editable@
        return  
    #delete the node after the node containting value u
    # error message: Node to delete after not found
    def deleteAfter(self,u):
        #@start-editable@
        f=0
        if(self.sz==0 or (self.sz==1 and self.head.element==u)):
          f=1
          return None
        elif(self.sz==1 and self.head.element!=u):
          return None
        elif(self.sz==2 and self.head.element==u):
          self.deleteLast()
          return
        elif(self.sz==2 and self.head.next.element==u):
          f=1
          return None
        elif(self.sz==2 and self.head.element!=u and self.head.next.element!=u):
          f=0
        else:
          curnode=self.head
          while(curnode.next.next!=None):
            if(curnode.element==u):
              temp=curnode.next
              curnode.next=temp.next
              temp.next.prev=curnode
              temp.prev=None
              temp.next=None
              self.sz-=1
              f=1
              break
            curnode=curnode.next
          if(f!=1):
            tnode=self.tail.prev
            if(tnode.element==u):
              self.deleteLast()
              f=1
              return
          if(self.tail.element==u):
            return None
        if(f==0):
          print("Node to delete after not found")
            
    #@end-editable@
        return
    #delete the node before the node containting value u
    # error message: Node to delete before not found
    def deleteBefore(self,u):
        #@start-editable@
        f=0
        if(self.head.element==u):
          return None
        if(self.sz==0 or (self.sz==1 and self.head.element==u)):
          f=1
          return None
        elif(self.sz==2 and self.head.element==u):
          f=1
          return None
        elif(self.sz==2 and self.head.next.element==u):
          self.deleteFirst()
          return
        elif(self.sz==1 and self.head.element!=u):
          return None
        elif(self.sz==2 and self.head.element!=u and self.head.next.element!=u):
          f=0
        else:
          tnode=self.head.next
          if(tnode.element==u):
            self.deleteFirst()
            f=1
            return
          tnode=tnode.next
          while(tnode!=None):
            if(tnode.element==u):
              temp=tnode.prev
              temp.prev.next=tnode
              tnode.prev=temp.prev
              temp.prev=None
              temp.next=None
              self.sz-=1
              f=1
              break
            tnode=tnode.next
        if(f==0):
          print("Node to delete before not found")
            
    #@end-editable@
        return
    def findNode(self, val):
        #@start-editable@
        curnode=self.head
        while(curnode!=None):
          if(curnode.element==val):
            return curnode
          curnode=curnode.next
            
    #@end-editable@
        return
    #swap the nodes containing u and v
    def swap(self,u,v):
        #@start-editable@
        fnode=self.head
        snode=self.head
        c=0
        while(fnode!=None):
          if(fnode.element==u):
            c=1
            break
          fnode=fnode.next
        if(c==1):
          while(snode!=None):
            if(snode.element==v):
              c=2
              break
            snode=snode.next
        else:
          return None
        if(c==2):
          temp=fnode.element
          fnode.element=snode.element
          snode.element=temp
            
    #@end-editable@
        return
 
    def isEmpty(self):
        #@start-editable@
            
            
    #@end-editable@
        return (self.sz==0)
    def size(self):
        #@start-editable@
            
            
    #@end-editable@
        return self.sz
    def printList(self):
        if (self.isEmpty()):
            print ("Linked List Empty Exception")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print(" ")
            tnode = self.tail
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.prev
            print(" ")
        return
    
def testDLL():
    dll = DLList()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(dll.size())
        elif(operation[0]=="I"):
            print(dll.isEmpty())
        elif(operation[0]=="IF"):
            dll.insertFirst(int(operation[1]))
            dll.printList()
        elif(operation[0]=="IL"):
            dll.insertLast(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DF"):
            dll.deleteFirst()
            dll.printList()
        elif(operation[0]=="DL"):
            dll.deleteLast()
            dll.printList()
        elif(operation[0]=="IA"):
            dll.insertAfter(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="IB"):
            dll.insertBefore(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="DA"):
            dll.deleteAfter(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DB"):
            dll.deleteBefore(int(operation[1]))
            dll.printList()   
        elif(operation[0]=="F"):
            print(dll.getHead().element)
        elif(operation[0]=='L'):
            print(dll.getLastNode().element)
        elif(operation[0]=='FIND'):
            temp = dll.findNode(int(operation[1]))
            if (temp!=None):
                print(temp.element)
            else:
                print("NULL")
        elif(operation[0]=='SW'):
            dll.swap(int(operation[1]),int(operation[2]))
            dll.printList()
        inputs-=1

def main():
    testDLL()
if __name__ == '__main__':
    main()