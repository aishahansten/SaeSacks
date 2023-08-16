a = int(input())
sentence = list(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphalist = []
alphanumlist = []
stack = [0] * 100
top = -1
for k in alpha:
    alphalist.append(k)
    alphanumlist.append(k)
#print(alphalist)

for i in range(a):
    alphanumlist[i] = int(input())
#print(alphanumlist)
for i in range(len(sentence)):
    for j in range(len(alphalist)):
        if sentence[i] == alphalist[j]:
            sentence[i] = alphanumlist[j]
#print(sentence)
for i in sentence:
    if i =='*' or i =='/' or i =='+' or i =='-' :
        op1 = stack[top]
        top -= 1
        op2 = stack[top]
        top -= 1
        if i == '+':
            top += 1
            stack[top] = op2 + op1
        elif i == '-':
            top += 1
            stack[top] = op2 - op1
        elif i == '*':
            top += 1
            stack[top] = op2 * op1
        elif i == '/':
            top += 1
            stack[top] = op2 / op1
    else:
        top += 1
        stack[top] = int(i)
#print(stack)
print(f'{stack[top]:.2f}')




