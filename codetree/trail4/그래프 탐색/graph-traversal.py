N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(curr_num):
    for elem in adj_list[curr_num]:
        if not visited[elem]:
            visited[elem] = True
            dfs(elem)


for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

visited[1] =True
dfs(1)
print(sum(visited)-1)