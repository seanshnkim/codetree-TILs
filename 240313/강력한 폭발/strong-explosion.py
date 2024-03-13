import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

to_be_bombed = []
which_bomb = {}
for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            to_be_bombed.append((r,c))

# key에는 폭탄의 위치(행, 열), 
# value에는 어떤 종류의 폭탄을 넣을지(1~3, 0은 초기화 상태)
which_bomb = {bomb_pos:0 for bomb_pos in to_be_bombed}

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def moves(opt):
    if opt == 1:
        drs = [-2, -1, 1, 2]
        dcs = [ 0,  0, 0, 0]
    elif opt == 2:
        drs = [0, -1, 0, 1]
        dcs = [-1, 0, 1, 0]
    else:
        drs = [-1, -1, 1,  1]
        dcs = [-1,  1, 1, -1]
    
    return drs, dcs


def explode(to_be_bombed):
    # cnt = len(to_be_bombed)
    bombed = to_be_bombed.copy()
    for br, bc in to_be_bombed:
        opt = which_bomb[(br, bc)]
        drs, dcs = moves(opt)
        for dr, dc in zip(drs, dcs):
            if in_range(br+dr, bc+dc) \
            and (br+dr, bc+dc) not in bombed:
                # grid[br+dr][bc+dc] = 1
                # 이것도 아냐
                bombed.append((br+dr, bc+dc))
                # cnt += 1
    # return cnt
    return len(bombed)


# cnt -> 폭탄의 개수. 0부터 시작
def solution(cnt):
    if cnt == len(to_be_bombed):
        return explode(to_be_bombed)
    
    br, bc = to_be_bombed[cnt]
    max_cnt = 0

    for opt in range(1, 4):
        which_bomb[(br, bc)] = opt
        max_cnt = max(max_cnt, solution(cnt+1))
        which_bomb[(br, bc)] = 0

    return max_cnt

print(solution(0))