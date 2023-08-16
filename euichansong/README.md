### solved problem
#### [문제 깃헙] / [문제 백준 링크]
#### [BOJ_10826](https://github.com/aishahansten/SaeSacks/tree/master/euichansong/BOJ/%5B10826%5D%20%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98%EC%88%98%204%20%2B%20readme) / [피보나치 수 4](https://www.acmicpc.net/problem/10826)
#### [BOJ_1918](https://github.com/aishahansten/SaeSacks/tree/master/euichansong/BOJ/%5B1918%5D%20%ED%9B%84%EC%9C%84%20%ED%91%9C%EA%B8%B0%EC%8B%9D) / [후위 표기식](https://www.acmicpc.net/problem/1918)
#### [BOJ_1935](https://github.com/aishahansten/SaeSacks/tree/master/euichansong/BOJ/%5B1935%5D%20%ED%9B%84%EC%9C%84%20%ED%91%9C%EA%B8%B0%EC%8B%9D2) / [후위 표기식2](https://www.acmicpc.net/problem/1935)

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