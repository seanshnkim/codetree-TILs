import sys
input = sys.stdin.readline

N = int(input())
movements = []
for _ in range(N):
    dir, dist = input().split()
    dist = int(dist)
    movements.append((dir, dist))

# 남 서 북 동 -> 하지만 이건 2차원 보드 위에 있을 때 해당한다. (틀린 이유)
# 동 남 서 북 -> 2차원 좌표평면에 있을 떄
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


loc_x, loc_y = 0, 0
dir_num = 0
for dir, dist in movements:
    if dir == 'N':
        dir_num = 3
    elif dir == 'E':
        dir_num = 0
    elif dir == 'W':
        dir_num = 2
    else:
        dir_num = 1
    
    loc_x += dx[dir_num] * dist
    loc_y += dy[dir_num] * dist

print(loc_x, loc_y)