def isort(A):
    length=len(A)
    for x in A:
        if x > 1000 or x < 1:
            return
    if length > 0 and length <= 1000:
        for i in range(len(A)):
            j=i-1
            while(j >= 0) and (A[j] > A[j+1]):
                A[j],A[j+1] = A[j+1],A[j]
                j -= 1
    return    



if __name__ == "__main__": 
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]