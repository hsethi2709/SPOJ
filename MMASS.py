def push(num,stack):
    stack.append(num)

def peek(stack):
    if(len(stack)==0):
        return -1
    else:
        return stack[len(stack)-1]
mol=input().strip()
molmass={'H':1,'O':16,'C':12,'(':'('}
total_mass=0
stack=[]
for i in range(len(mol)):
    if(mol[i] in molmass or mol[i]=='('):
        push(molmass[mol[i]],stack)
    elif(mol[i].isnumeric()):
        n=int(peek(stack))
        stack.pop()
        push((n*int(mol[i])),stack)
    elif(mol[i]==')'):
        mass=0
        while(peek(stack)!='('):
            mass+=int(peek(stack))
            stack.pop()
        stack.pop()
        push(mass,stack)

while(peek(stack)!=-1):
    total_mass+=int(peek(stack))
    stack.pop()

print(total_mass)
