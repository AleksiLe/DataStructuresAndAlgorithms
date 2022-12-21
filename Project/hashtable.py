import time
class Node:#single node
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next


class LinkedList:#single nodes in linkedlist
    def __init__(self):  
        self.head = None
        self.len = 0

    def delete(self,index): #Deletes data from index
            iter=0
            if (index>self.len):
                return
            elif (self.len > 1):
                current=self.head
                if index!=0:
                    while(current):
                        if iter == index:
                            temp.next=current.next
                            current=None
                            self.len -= 1
                            return
                        temp=current
                        current=current.next
                        iter+=1 
                else:
                    self.head=current.next
                    current=None
                    self.len -= 1
            else:
                self.head = None
                self.len -= 1

                
    def append(self, data): #Adds new node to the beginning of the linked list.
        newNode = Node(data)
        if(self.head):
            current = self.head
            current.data =  self.head.data
            self.head=newNode
            self.head.next = current
            self.len += 1
        else:
            self.head = newNode
            self.len += 1
    
    def index(self,data): #Returns index where data is
        if (self.head):
            current = self.head
            iter=0
            while(current):
                if data==current.data:
                    return iter
                iter+=1
                current=current.next
            return -1

    def print(self): #Prints linked list
        if self.head == None:
            return
        current = self.head
        lister=[]
        while(True):
            lister.append(current.data)
            current = current.next
            if current == None:
                return lister
        


class HashTable: #Produses array for hash table and functions to support it
    def __init__(self,len = None):
        self.len = len
        self.array = [None] * len
    
    def procedureHash(self,data): #Hash function
        sum = 0
        if type(data) is int:
            data = str(data)
        for i in data:
            sum += ord(i)**3
        return sum % self.len
    
    def insert(self,data): #Creates linkedlist to empty index or adds data to linkedlist
        iter = self.procedureHash(data)
        if self.array[iter]==None:
            self.array[iter]=LinkedList()
            self.array[iter].append(data)
        elif self.array[iter]!=None:
            firstNode=self.array[iter]
            firstNode.append(data)
    
    def printer(self): #Prints the whole hashtable
        lister=[]
        for i in range(0,self.len):
            if self.array[i]==None:
                lister.append(None)
            else:
                x=self.array[i].print()
                lister.append(x)
        print(lister)

    def delete(self,data): #Finds index for data and deletes it
        iter = self.procedureHash(data)
        linkedList = self.array[iter]
        index = linkedList.index(data)
        linkedList.delete(index)

    def search(self,data): #Looks if data exists inside the hash table
        iter = self.procedureHash(data)
        if self.array[iter] == None:
            return -1
        linkedList = self.array[iter]
        index = linkedList.index(data)
        if index == -1:
            return -1
        else:
            return 1

def main(): #Calculates time for initializing hashtable, adding the words to hashtable and finding same words
    start_time = time.time()
    hashtable = HashTable(10000)
    print("Initialize the hash table", time.time()-start_time)
    start_time = time.time()
    f = open("words_alpha.txt", "r",encoding="utf-8")
    counter = 0
    for l in f:
        hashtable.insert(l)
    f.close()
    print("Adding the words", (time.time()-start_time))
    start_time = time.time()
    ff = open("kaikkisanat.txt","r",encoding="utf-8")
    for l in ff:
        index = hashtable.search(l)
        if index == 1:
            counter += 1
    ff.close()
    print("Finding common words", time.time()-start_time)
    print("Matches", counter)

main()