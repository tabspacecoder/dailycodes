class node:
     def __init__(self,e=None,next=None, prev = None):
          self.element = e
          self.next = next
          self.prev = prev
          
class DLList:
     def __init__(self):
          self.head = None
          self.tail = None 
          self.sz = 0
          
          
     def insertLast(self,e):
          newnode=node(e)
          if self.head ==None:
              self.head=newnode
              self.tail=newnode
          else:
              temp=self.tail
              newnode.prev=temp
              self.tail.next=newnode
              self.tail=newnode
          return

     def insertFirst(self,e):
          
          return

    
     
     def deleteFirst(self):
          
          return

     def deleteLast(self):
          
          return

          
     def printListForward(self):
          tnode = self.head
          while tnode!= None:
               print(tnode.element,end=" ")
               tnode = tnode.next
          print("")
          return

     def printListBackward(self):
          tnode = self.tail

          while tnode!= None:
               print(tnode.element,end=" ")
               tnode = tnode.prev
          #print(tnode.element)
          print("")
          return
     
     def findNode(self, val):
          curnode = self.head
          while curnode!=None:
               if curnode.element == val:
                    return curnode
               curnode = curnode.next
          return None
     
     def isEmpty(self):
          return self.sz==0

     def size(self):
          return self.sz


     
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
            dll.printListForward()
        elif(operation[0]=="IL"):
            dll.insertLast(int(operation[1]))
            dll.printListBackward()
            dll.printListForward()
        elif(operation[0]=="DF"):
            dll.deleteFirst()
            dll.printListForward()
        elif(operation[0]=="DL"):
            dll.deleteLast()
            dll.printListForward()


           
        
        inputs-=1


def main():
    testDLL()

if __name__ == '__main__':
    main()
