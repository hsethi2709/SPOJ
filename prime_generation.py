import math
t=int(input())
for z in range(t):
    lower,upper=map(int,input().split())
    def simple_sieve(n,arr):
        a=[True]*(n+1)
        p=2
        while(p*p<=n):
            if(a[p]==True):
                for i in range(p*2,n+1,p):
                    a[i]=False
            p+=1

        for i in range(2,n):
            if(a[i]):
                arr.append(i)


    limit=math.floor(math.sqrt(upper))+1
    arr=[]
    simple_sieve(limit,arr)
    if(lower<limit):
        index=0
        while(arr[index]<lower):
            index+=1
        for i in range(index,len(arr)):
            print(arr[i])
        low=limit
    else:
        low=lower
    high=low+limit

    while(low<upper):
        if(high>upper):
            high=upper+1
        mark=[True]*(limit)
        for i in range(len(arr)):
            lowmin=(low//arr[i])*arr[i]
            if(lowmin<low):
                lowmin+=arr[i]
            for j in range(lowmin,high,arr[i]):
                mark[j-low]=False
        for i in range(low,high):
            if(mark[i-low]==True):
                print(i)

        low+=limit
        high+=limit
