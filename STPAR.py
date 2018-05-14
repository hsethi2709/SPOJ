def push(num,stack):
        stack.append(num)

def peek(stack):
    if(len(stack)==0):
        return -1
    return stack[len(stack)-1]

results=[]
n=int(input())
while n!=0:
    incoming_cars = list(map(int, input().split()))
    car=1
    i=0
    main = []
    sidestreet = []

    while(i<len(incoming_cars) or car<=n):
        if(i<len(incoming_cars) and car==incoming_cars[i]):
                main.append(car)
                i=i+1
                car+=1
        elif(peek(sidestreet)==car):
            main.append(car)
            sidestreet.pop()
            car+=1
        elif(i<len(incoming_cars)):
            push(incoming_cars[i],sidestreet)
            i+=1
        else:
            break

    if(len(main)!=n):
        results.append("no")
    else:
        results.append("yes")
    n = int(input())
print(*results,sep="\n")

