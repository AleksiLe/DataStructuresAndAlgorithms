
def split(T):
    counter=0
    limit=0
    midcounter=0
    highcounter=0
    for i in range(0,len(T)):
        if i<=len(T)-2:
            if T[i] > T[i+1]:
                limit=i
                midcounter+=1
            if T[i] <= T[i+1]:
                if highcounter<midcounter:
                    highcounter=midcounter
                midcounter=0


                
    T.reverse()
    
    for i in range(0,len(T)):
        if T[i] < limit:
            break
        if i<=len(T)-2:   
            if T[i] > T[i+1]:
                counter+=1
    if highcounter < counter:
                highcounter=counter
    return counter

print(split([1, 2, 3, 4, 4, 6, 5, 7, 9, 8, 7, 8]))
        
        
