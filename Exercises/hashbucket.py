

class HashBucket:
    def __init__(self,len = None,bucket = None):
        self.len = len
        self.bucket = bucket
        self.lenbucket = len//bucket
        self.overflowArray = [None] * len
        self.array = [None] * len
    
    def procedureHash(self,data):
        sum = 0
        for i in data:
            sum += ord(i)
        return sum % self.bucket

    def insert(self,data):
        iter = self.procedureHash(data)
        for i in range((iter*self.lenbucket),((iter+1)*self.lenbucket)):
            if self.array[i] == data:
                return
            elif self.array[i] == None or self.array[i] == -1:
                self.array[i] = data
                return
        for i in range(0,self.len-1):
            if self.overflowArray[i] == data:
                return
            elif self.overflowArray[i] == -1 or self.overflowArray[i] == None:
                self.overflowArray[i] = data
                return

            
    def delete(self,data):
        iter = self.procedureHash(data)
        for i in range((iter*self.lenbucket),((iter+1)*self.lenbucket)):
            if self.array[i] == data:
                self.array[i] = -1
                return
            elif self.array[i] == None:
                break
            
        for i in range(0,self.len-1):
            if self.overflowArray[i] == data:
                self.overflowArray[i] = -1
                return
            elif self.overflowArray[i] == None:
                break
    
    def print(self):
        arr=[]
        for i in self.array:
            if i == -1 or i == None:
                continue
            else:
                arr.append(i)
        for i in self.overflowArray:
            if i == -1 or i == None:
                continue
            else:
                arr.append(i)
        print(*arr,sep=' ')
 

            