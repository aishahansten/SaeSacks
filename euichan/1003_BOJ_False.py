
def fibo(n):
    # cnt0 = 0
    global cnt1
    global f
    if n >= 2 and f[n] == 0:
        f[n] = fibo(n-1) + fibo(n-2)
        if f[n] == 1 or fibo(n-1) == 1 or fibo(n-2) ==1:
            cnt1 += 1
    return f[n]

t = int(input())

for i in range(t):
    n = int(input())
    cnt1 = 0
    f = [0] * (n + 2)
    f[0] = 0
    f[1] = 1
    fibo(n)
    print(cnt1, cnt1+1)