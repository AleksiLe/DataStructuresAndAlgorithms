
def pairs(s):
    counter = 0
    oneCounter = -1
    
    for i in range(0,len(s)):
        if s[i] == '1':
            for i in range(i,len(s)):
                oneCounter+=1
                if s[i] == '1':
                    counter+=oneCounter
                    print(oneCounter)
            oneCounter=-1
    return counter
        
        

    
    
print(pairs("1001001"))
print(pairs("1001001001")) # 71


    


