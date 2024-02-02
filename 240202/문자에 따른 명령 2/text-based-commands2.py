import sys
input = sys.stdin.readline

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
# North = 3 / East = 0 / West = 2 / South = 1
dir_num = 3

order = input()

for ord in order:
    if ord == 'L':
        dir_num = (dir_num + 3) % 4
    elif ord == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)