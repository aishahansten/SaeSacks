## [BOJ_10826](깃헙링크) 피보나치 수 4
[BOJ_1234](https://github.com/SeongukBaek/algoStudy/tree/main/BOJ/%5B10282%5D%20%ED%95%B4%ED%82%B9/SUbbb)
### 📌 Algorithm

D.P

### 📍 Logic
```python
def fibo(n):
    fibo = [0,1,1]
    for i in range(3,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n]
t = int(input())
print(fibo(t))
```

### ✒️Review
- 리스트에 append 하는 방법이 있고, 0으로된 배열을 만들어 값들을 넣어주는 방법이 있다.
- recursive방식과 iterative방식은 잘 이해가 안간다
- 참고: https://github.com/SeongukBaek/algoStudy/tree/main