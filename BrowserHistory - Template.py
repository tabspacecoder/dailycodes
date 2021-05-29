class Stack:
    
    def __init__(self,max_stack_size):
        self.stack = [None]*max_stack_size
        # this is the stack container called 'stack'
        self.max_stack_size = max_stack_size
        # define the stack size 'max_stack_size' and initialize it
        self.t = -1
        self.enable=1

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        if (self.size() == self.max_stack_size):
           return -1
        else:
            self.t= self.t+1
            self.stack[self.t] = value            
        return
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if (self.size() == 0):
            return -1
        else:
            toret = self.stack[self.t]
            self.stack[self.t] = None
            self.t = self.t-1
            return (toret)
        
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        if (self.size() == 0):
              return -1
        else:
            return self.stack[self.t]
        

    # returns True if stack is empty   
    def isEmpty(self):
        return  (self.t<0)

    # returns the number of elements currently in stack 
    def size(self):
        return (self.t+1)
        
    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            for i in range(self.max_stack_size):
                if self.stack[i]!=None:
                   print(self.stack[i],end=" ")                
            print(" ")
        

    def Visitpage(self,dname):
        if self.enable==1:
            if self.size() == self.max_stack_size:
                print("HistoryFullException")
            else:
                self.push(dname)
                self.printStack()
        else:
            print("Operation is not allowed")


    def Recentlyvisitedpage(self):
        if self.enable == 0:
            if self.isEmpty():
                print("HistoryisEmpty")
            else:
                temp = self.top()
                print(temp)
                if self.size() == self.max_stack_size:
                    print("HistoryFullException")
                else:
                    self.push(temp)
                    self.printStack()
        else:
            print("Operation is not allowed")


    def Loadnthvisitedpage(self,n):
        if self.enable == 0:
            if self.isEmpty():
                print("HistoryisEmpty")
            else:
                temp = self.stack[self.t - n + 1]
                print(temp)
                if self.size() == self.max_stack_size:
                    print("HistoryFullException")
                elif n > self.size():
                    print("NotAvailable")
                else:
                    self.push(temp)
                    self.printStack()
        else:
            print("Operation is not allowed")


    def Clearhistory(self,n):
        if self.enable==1:
            for i in range(n):
                if self.size() == 0:
                    print("HistoryisEmpty")
                else:
                    self.pop()
            else:
                self.printStack()
        else:
            print("Operation is not allowed")



    def Enablehistory(self):
        self.enable=1
        
    def Disablehistory(self):
        self.enable=0
         
     

def teststack():
    stackmaxsize = int(input())
    st1 = Stack(stackmaxsize)
    N = int(input())  #no. of operations
    while (N > 0):
        temp = input().split()
        if (temp[0]=='E'):
            st1.Enablehistory()
        elif (temp[0]=='D'):
            st1.Disablehistory()    
        elif (temp[0]=='V'):            
            st1.Visitpage(temp[1])
        elif (temp[0]=='R'):
            st1.Recentlyvisitedpage()
        elif(temp[0]=='L'):
            st1.Loadnthvisitedpage(int(temp[1]))
        elif(temp[0]=='C'):
            st1.Clearhistory(int(temp[1]))
        N=N-1
    

def main():
    teststack()

if __name__ == '__main__':
    main()
