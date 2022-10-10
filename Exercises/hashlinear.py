class HashLinear:
    def __init__(self,len = None):
        self.len = len
        self.array = [None] * len
    
    def procedureHash(self,data):
        sum = 0
        for i in data:
            sum += ord(i)
        return sum % self.len

    def insert(self,data):
        iter = self.procedureHash(data)
        counter = 0
        while(True):
            if self.array[iter] == data:
                break
            elif self.array[iter] == None:
                self.array[iter] = data
                return
            elif self.array[iter] == -1:
                self.array[iter] = data
                return
            else:
                iter +=1
                if iter >= self.len:
                    iter = 0
            counter +=1
            if counter==self.len:
                break
    
    def delete(self,data):
        iter = self.procedureHash(data)
        counter = 0
        while(True):
            if self.array[iter] == None:
                break
            elif self.array[iter] == -1:
                iter+=1
            elif self.array[iter] == data:
                self.array[iter] = -1
            else:
                iter +=1
                if iter >= self.len:
                    iter = 0
            counter +=1
            if counter==self.len:
                break 
    
    def print(self):
        arr=[]
        for i in self.array:
            if i == -1 or i == None:
                continue
            else:
                arr.append(i)
        print(*arr,sep=' ')

    

            