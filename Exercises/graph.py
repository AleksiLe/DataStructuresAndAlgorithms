class Graph:
    def __init__(self, matrix = None):
        self.matrix=matrix
        self.gr_list=self.graph_list()
        self.vr_list=self.vertex_list()

    def vertex_list(self):
        weight_lst=self.gr_list
        complete = []
        part = []
        iter = 0
        for i in weight_lst:
            if type(i) == int:
                pass
            else:
                for j in i:
                    if [j[0],j[1],iter] in complete:
                        pass
                    else:
                        part=[iter,j[1],j[0]]
                        complete.append(part)
                        part=[]
            iter+=1
        complete.sort(key=lambda x: x[1])
        return complete
    
    def graph_list(self):
        holder2=[]
        holder=[]
        graphList=[]
        for i in self.matrix:
            for j in range(0,len(i)):
                if i[j]!=0:
                    holder2=[j,i[j]]
                    holder.append(holder2)
                    holder2=[]
            if holder == []:
                holder.append(0)
            graphList.append(holder)
            holder=[]
        return graphList
                

    def df_print(self, index = None):
        next_steps=self.matrix[index]
        history=[index]
        marked=[index]
        while (True):
            for i in range(0,len(next_steps)):
                if next_steps[i]!=0:
                    if i in marked:
                        if i == len(next_steps)-1:
                            if len(history) == 0:
                                print(*marked, sep=' ')
                                return
                            next_steps=self.matrix[history[len(history)-2]]
                            history = history[:-1]
                        else:
                            pass
                    else:
                        marked.append(i)
                        history.append(i)
                        next_steps=self.matrix[i]
                        break
                if i == len(next_steps)-1:
                    if len(history) == 0:
                        print(*marked, sep=' ')
                        return
                    next_steps=self.matrix[history[len(history)-2]]
                    history = history[:-1]
                    break
            if len(marked) == len(next_steps):
                break
        print(*marked, sep=' ')

    def bf_print(self, index=None):
        grlist=self.gr_list
        ind=index
        queue=[]
        temp=[]
        history=[]
        while True:
            for i in grlist[ind]:
                if type(i) is int:
                    pass
                elif i[1]!=None:
                    if (i[0] in queue) or (i[0] in history):
                        pass
                    else:
                        temp.append(i[0])
            temp.sort()
            queue.extend(temp)
            temp=[]
            history.append(ind)
            if len(history)==len(grlist):
                print(*history,sep=' ')
                break
            try:
                ind=queue[0]
            except Exception:
                print(*history,sep=' ')
                return
            queue=queue[1:]

    def weight(self, index1=None,index2=None):
        grlist=self.gr_list
        for i in grlist[index1]:
            if type(i) == int:
                return -1 
            elif index2 == i[0]:
                return i[1]
        return -1
        
if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 6, 9, 0], # 0
        [0, 0, 5, 0, 0, 6], # 1
        [7, 5, 0, 1, 0, 2], # 2
        [6, 0, 1, 0, 0, 2], # 3
        [9, 0, 0, 0, 0, 1], # 4
        [0, 6, 2, 2, 1, 0]  # 5    
    ]
    graph = Graph(matrix)
    graph.vertex_list()
