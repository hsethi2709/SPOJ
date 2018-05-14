def push(num,arr):
        arr.append(num)
        return arr
def peek(arr):
    return arr[len(arr)-1]


operator=['#','(',')','+','-','*','/','^']


t=int(input())
results=[]
for i in range(t):
    postfix=[]
    stack=['#']
    expression=input()
    for j in expression:
        if j not in operator:
            postfix.append(j)
        else:
            if(j=='('):
                stack=push(j,stack)
            elif(j==')'):
                while(peek(stack)!='('):
                    postfix.append(stack.pop())
                else:
                    stack.pop()
            else:
                if(operator.index(j)>operator.index(peek(stack))):
                    stack=push(j,stack)
                else:
                    while(operator.index(j)<=operator.index(peek(stack))):
                        postfix.append(stack.pop())
                    push(j,stack)

    while(peek(stack)!='#'):
        postfix.append(stack.pop())

    results.append(''.join(map(str,postfix)))

print(*results,sep="\n")
