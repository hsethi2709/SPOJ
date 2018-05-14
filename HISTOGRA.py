def push(num,stack):
    stack.append(num)

def peek(stack):
    if(len(stack)==0):
        return -1
    else:
        return stack[len(stack)-1]

results=[]
stack=[]
while True:
    heights=list(map(int,input().split()))
    if(heights[0]==0):
        break

    max_area=0
    i=1
    area = 0
    while(i<heights[0]):
        if(len(stack)==0 or heights[i]>=heights[peek(stack)]):
            push(i,stack)
            i+=1
        else:

                tp=peek(stack)
                stack.pop()
                if(len(stack)==0):
                    area=heights[tp]*(i-1)
                else:
                    area=heights[tp]*(i-peek(stack)-1)
                if (area > max_area):
                    max_area = area

    while(peek(stack)!=-1):

        tp=peek(stack)
        stack.pop()
        if (peek(stack) == -1):
            area = heights[tp] * i
        else:
            area = heights[tp] * (i - peek(stack) - 1)

        if(area>max_area):
            max_area=area
    results.append(max_area)


print(*results,sep="\n")

