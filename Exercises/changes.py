def changes(A):
    counter=0
    if len(A) < 1 or len(A) >10**6:
        return False
    else:
        if A[0] < 1 or A[0] >10**3:
                return False
        for i in range(1,len(A),2):
            if A[i] < 1 or A[i] >10**3:
                return False
            elif i<=len(A)-5 and A[i+2]==A[i+3] and A[i+4]==A[i+3]:
                A[i+3]=A[i+2]+1
                counter+=1
            if i==len(A)-1:
                if A[i-1] == A[i]:
                    counter+=1
            elif A[i-1] == A[i] or A[i+1] == A[i]:
                counter+=1
        return counter

print(changes([1 for _ in range(100)]))






                    

