
def search(A: list, item: int):
    bottom=0
    high=len(A)-1
    half=bottom+(high-bottom)//2
    
    while(bottom<=high):
        if A[half]==item:
            return half
        elif A[half]<item:
            bottom=half+1
        else:
            high=half-1
        half=bottom+(high-bottom)//2
    return -1




if __name__ == "__main__":
    A = [1, 2, 3, 6, 10, 15, 22, 27, 30, 31]
    print(search(A, 6))     # 3
    print(search(A, 7))     # -1
    print(search(A, 30))    # 8

