from collections import deque

m, n = tuple(map(int, input().split()))

box = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

days = [
    [0] * m
    for _ in range(n)
]

q = deque()

# visited, days 세팅
answer_0_flag = True

for r in range(n):
    for c in range(m):
        if box[r][c] == -1:
            visited[r][c] = True
            days[r][c] = -1
        if box[r][c] == 0:
            answer_0_flag = False


drs, dcs = [1, -1, 0, 0], [0, 0, 1, -1]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

def can_go(r, c):
    return in_range(r, c) and not visited[r][c]

def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc

            if can_go(nr, nc) and box[nr][nc] == 0:
                visited[nr][nc] = True
                days[nr][nc] += (days[r][c] + 1)
                box[nr][nc] = 1
                q.append((nr, nc))


# 토마토 익는 과정 수행
for r in range(n):
    for c in range(m):
        if box[r][c] == 1:
            visited[r][c] = True
            days[r][c] = 0 # 없어도 되는 코드
            q.append((r, c))
bfs()


# 결과 분석
max_days = 0

def analyze_result():
    global max_days

    if answer_0_flag:
        return 0

    for r in range(n):
        for c in range(m):
            max_days = max(days[r][c], max_days)
            if box[r][c] == 0:
                return -1
    return max_days


print(analyze_result())