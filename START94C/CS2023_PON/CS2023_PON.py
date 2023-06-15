T = int(input())
for _ in range(T):
    N,B = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    
    c = len(bin(max(arr))[2:])
    
    reqnum = bin(B)[2:]
    reqnum = ((c-len(reqnum))*"0")+reqnum
    
    binarr = []
    for ele in arr:
        binnum = bin(ele)[2:]
        binnum = ((c-len(binnum))*"0")+binnum
        binarr.append(binnum)
    
    allowedsubseq = set(range(N))
    for j in range(c):
        for i in range(0,len(binarr)):
            if binarr[i][j] == "0" and reqnum[j]=="1":
                try:
                    allowedsubseq.remove(i)
                except:
                    continue
    
    allowedsubseq = list(allowedsubseq)
    if len(allowedsubseq) == 0:
        print("NO")
    else:
        andd = arr[allowedsubseq[0]]
        for ele in allowedsubseq:
            andd = arr[ele]&andd
            
        #print(andd)
        if andd == B:
            print("YES")
        else:
            print("NO")