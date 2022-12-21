from graph import Graph

def kruskal(graph):
    weight_lst=graph.vr_list
    history = []
    history1=[]
    wg=[]
    for i in weight_lst:
        if i[0] in history and i[2] in history:
            pass
        elif i[0] in history:
            if i[2] in history1:
                history.extend(history1)
                history.append(i[2])
                wg.append(i)
            else:
                history.append(i[2])
                wg.append(i)
        elif i[2] in history:
            if i[0] in history1:
                history.extend(history1)
                history.append(i[0])
                wg.append(i)
            else:
                history.append(i[0])
                wg.append(i)
        elif history==[]:
            history.append(i[0]) 
            history.append(i[2])
            wg.append(i)
        else:
            history1.append(i[0]) 
            history1.append(i[2])
            wg.append(i)
    length = len(graph.matrix)
    
    for i in range(length):
        for j in range(length):
                if [i,graph.matrix[i][j],j] in wg:
                    pass
                elif[j,graph.matrix[i][j],i] in wg:
                    pass
                else:
                    graph.matrix[i][j] = 0
    print(graph.matrix)
    return Graph(graph.matrix)
    

    
 
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
    graph.bf_print(0)   # 0 2 3 4 1 5
    mst = kruskal(graph)
    mst.bf_print(0)     # 0 3 2 1 5 4