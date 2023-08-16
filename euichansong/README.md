### solved problem

#### [BOJ_10826](깃헙링크) / [피보나치 수 4](https://www.acmicpc.net/problem/10826)
#### [BOJ_1918](깃헙링크) / [후위 표기식](https://www.acmicpc.net/problem/1918)
#### [BOJ_1935](깃헙링크) / [후위 표기식2](https://www.acmicpc.net/problem/1935)

### 📌 Today Algorithm

Stack

### 📍 Today Logic
```python
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


```

### ✒️Review
- a
- b
- 참고: https://github.com/SeongukBaek/algoStudy/tree/main