#n은 시작정점
#v는 정점 갯수
#adj는 간선 표현

"""
V E
v1 w1 v2 w2 .....
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 1 2 가 연결된 경우 2차원 배열로 1,2 2,1에 1을 더해 표시한다 - 인접행렬
# 인접리스트도 있음- 강의 다시보기
"""

def dfs(n,v,adj_m):
    stack = []
    visited = [0] * (v+1)
    print(n)
    visited[n] = 1
    while True:
        for w in range(1, v+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                visited[w] = 1
                print(n)
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return

v, e = map(int, input().split())
arr = list(map(int, input().split()))
adj_m = [[0] * (v+1) for _ in range(v+1)]
for i in range(e):
    v1, v2 = arr[i * 2], arr[i * 2 + 1] # 0 1, 2 3, 4 5, 6 7, 8 9
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1,v,adj_m)