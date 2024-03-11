import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 최하단 격자의 좌표, 오른쪽과 왼쪽 이동 길이가 주어졌을 때, 합을 구한다.
def sum_tilted(r, c, right, left):
    # 현재 기준점은 (r, c). 즉 최하단 격자의 좌표
    cur_sum = 0
    # 1번 방향의 이동
    for i in range(right):
        dx, dy = -i, i
        cur_sum += grid[r+dx][c+dy]
    # 기준점을 이동시킨다.
    r -= right
    c += right
    # 2번 방향의 이동
    for i in range(left):
        dx, dy = -i, -i
        cur_sum += grid[r+dx][c+dy]
    # 기준점 이동
    r -= left
    c -= left
    # 3번 방향의 이동
    for i in range(right):
        dx, dy = i, -i
        cur_sum += grid[r+dx][c+dy]
    # 기준점 이동
    r += right
    c -= right
    # 4번 방향의 이동
    for i in range(left):
        dx, dy = i, i
        cur_sum += grid[r+dx][c+dy]
    
    return cur_sum

# 최하단 격자와 1번 변의 길이(오른쪽으로 몇 칸 이동?)가 주어졌을 때, 
# 가능한 기울어진 직사각형 중 최대 합을 구한다.
def max_tilted(r, c, right):
    cur_sum = 0
    max_left = min(r-1, c)
    for left in range(1, max_left+1):
        # 높이도 신경 써야지... 1시간 디버깅 -> 틀린 이유
        if r-left-right < 0:
            continue
        cur_sum = max(cur_sum, sum_tilted(r, c, right, left))
    
    return cur_sum

ans = 0
for r in range(2, N):
    for c in range(1, N-1):
        max_right = min(N-1-c, r-1)
        for right in range(1, max_right+1):
            ans = max(ans, max_tilted(r, c, right))
print(ans)