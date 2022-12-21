from graph import Graph
INF=999
def sort(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            x = matrix[i]
            if i == j:
                pass
            elif x[j]==0:
                x[j]=INF
    return matrix

def reverseSort(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            x = matrix[i]
            if i == j:
                pass
            elif x[j]==INF:
                x[j]=0
    return matrix

def floyd(graph):
    matrix = sort(graph.matrix)
    dist = list(map(lambda p: list(map(lambda q: q, p)), matrix)) 
    for r in range(len(graph.matrix)):
        for p in range(len(graph.matrix)):
            for q in range(len(graph.matrix)):
                if dist[p][r] + dist[r][q] == 0:
                    pass
                else:
                    dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    dist = reverseSort(dist)

    return dist

if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0], # 0
        [0, 0, 0, 0, 0, 0], # 1
        [0, 5, 0, 1, 0, 2], # 2
        [6, 0, 0, 0, 0, 2], # 3
        [0, 0, 0, 0, 0, 1], # 4
        [0, 6, 0, 0, 0, 0]  # 5   
    ]
    graph = Graph(matrix)
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()
    #  0 12  7  8  9  9 
    #  0  0  0  0  0  0 
    #  7  5  0  1 16  2 
    #  6  8 13  0 15  2 
    #  0  7  0  0  0  1 
    #  0  6  0  0  0  0 