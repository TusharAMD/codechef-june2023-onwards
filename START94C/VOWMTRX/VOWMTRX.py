#babylo nnian jiia
#babylon nian jiia
#babylonn ian jiia
#babylonn ianj iia

T = int(input())
for _ in range(T):
    N,K = [int(x) for x in input().split()]
    string = input()
    
    count = 0
    arr = []
    tempList = []
    for i in range(N):
        tempList.append(string[i])
        if string[i] in ("a","e","i","o","u"):
            count+=1
            if count == K:
                count = 0
                arr.append(tempList)
                tempList = []
    #arr.append(tempList)
    #print(arr)
    prodarr = []
    newcount = 0
    for i in range(1,len(arr)):
        for ele in arr[i]:
            if ele in ("a","e","i","o","u"):
                prodarr.append(newcount+1)
                newcount = 0    
                break
            else:
                newcount += 1
    #print(prodarr)
    prod = 1
    for ele in prodarr:
        prod = prod * ele
    print(prod%((10**9) + 7))