#Single node

class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# single head node
class LinkedList:
    def __init__(self):  
        self.head = None
        self.len = 0

    def insert(self,data,index):
        iter=0
        newNode = Node(data)
        if (index>self.len):
            print("Can't add to list")
        elif (index > 0):
            if (self.head):
                current=self.head
                while(current):
                    if iter == index:
                        newNode.next=temp.next
                        temp.next=newNode
                        self.len+=1
                        return
                    temp=current
                    current=current.next
                    if current == None:#you dont test this in tester but you cannot add to last value without this
                        current=newNode
                        self.len+=1
                    iter+=1
        else:
            if (self.head):
                current=self.head
                newNode.next=current
                self.head=newNode
                self.len+=1
            else:
                print("Can't add to list")

    def delete(self,index):
            iter=0
            if (index>self.len):
                return
            elif (self.len > 1):
                current=self.head
                if index!=0:
                    while(current):
                        if iter == index:
                            temp.next=current.next
                            self.len-=1
                            current=None
                            return
                        temp=current
                        current=current.next
                        iter+=1 
                else:
                    self.head=current.next
                    current=None
            else:
                self.node = None
                self.len-=1

                
    def append(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
            self.len+=1
        else:
            self.head = newNode
            self.len+=1
    
    def index(self,data):
        if (self.head):
            current = self.head
            iter=0
            while(current):
                if data==current.data:
                    return iter
                iter+=1
                current=current.next
            return (-1)
  
    def print(self):
        current = self.head
        lister=[]
        while(current):
            lister.append(current.data)
            current = current.next
        print(*lister,sep=' -> ')

