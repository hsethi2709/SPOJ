

results=[]
count=1
while True:
    steps = 0
    stack = []
    line=input().rstrip()
    if(line[0]=='-'):
        break

    for i in line:
        if len(stack):
            if(i=='}'):
                if(stack.pop()==i):
                    steps+=1
            else:
                stack.append(i)
        else:
            stack.append(i)
    if(len(stack)):
        steps+= (len(stack)//2)
        if(stack[0]=='}'):
            steps+=1


    print("%d. %d" % (count,steps))
    count+=1



