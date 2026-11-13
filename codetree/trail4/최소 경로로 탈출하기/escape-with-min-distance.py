from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

distance = [[0]*M for _ in range(N)]

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    # 격자 범위 안인지
    # 방문한적없고, 뱀 없을 때
    if in_range(x, y) and not visited[x][y] and board[x][y] == 1:
        return True
    else:
        return False

def bfs():
    q = deque()
    q.append((0, 0, 0))

    while q:
        x, y, curr_dis = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if can_go(nx, ny):
                visited[nx][ny] = True
                distance[nx][ny] = curr_dis + 1
                q.append((nx, ny, curr_dis+1))

visited[0][0] = True
bfs()

if visited[N-1][M-1]:
    print(distance[N-1][M-1])
else:
    print(-1)

        
                

