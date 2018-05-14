t=int(input())
results=[]
for z in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    end=n-1
    start=n-2
    while(arr[start]>=arr[end] and start>=0):
        start=start-1
        end=end-1

    if(arr[start]==arr[end] or start<0):
        results.append(-1)
        continue
    pos=end
    for i in range(end+1,n):
        diff=arr[i]-arr[start]
        if arr[i]-arr[start]>0 and arr[i]<arr[end] and arr[i]-arr[start]<=diff:
            diff=arr[i]-arr[start]
            pos=i


    temp = arr[pos]
    arr[pos] = arr[start]
    arr[start] = temp



    arr1=arr[start+1:n]
    arr1.sort()
    arr[start+1:n]=arr1


    results.append(''.join(map(str,arr)))
print(*(results),sep="\n")
