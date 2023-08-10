def fibo(n):
    fibo = [0,1,1]
    for i in range(3,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n]
t = int(input())
print(fibo(t))