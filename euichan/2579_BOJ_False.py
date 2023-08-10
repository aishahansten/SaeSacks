import sys
sys.stdin = open("2579.txt", "r")

"""
f1 은 [계단1값]
f2 은 [계단1값+계단2값, 계단2값]
f3 은 [-(계단1값+계단2값+3값), 계단2값+계단3값, 계단1값+3값]
        = f2리스트 + 3값 , f1리스트+3값,  -(연속된3개값)
"""
t = int(input())
stairlist = [int(input()) for _ in range(t+1)]
stairlist[0] = 0
print(stairlist)
def stair(n):
    sta = [0] * (n+1)
    sta[0] = 0
    sta[1] =
    sta[2] =

for i in range(t):
    sta[]