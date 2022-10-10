def primes(N):
    primelist=[2]#my answer depends on fact that we know first primenumber is 2
    if (2 <= N <= 10**5):
        for i in range(2,N+1):
            counter=0
            for y in primelist:
                if i % y != 0:
                    counter+=1
                    if len(primelist) == counter:
                        primelist.append(i)
                                
        return len(primelist)
    elif N == 1:
        primelist.clear()
        return
    else:
        print("Fail")
        return


if __name__ == "__main__":
    print(primes(0))    # 4
    print(primes(2))   # 6
    print(primes(10))   # 15