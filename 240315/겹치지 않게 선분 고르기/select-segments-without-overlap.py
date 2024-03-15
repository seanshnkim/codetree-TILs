import sys
input = sys.stdin.readline

N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

def intersect(seg1, seg2):
    a1, a2 = seg1
    b1, b2 = seg2

    if a2 < b1 or b2 < a1:
        return False
    else:
        return True

# 0번째 선분은 기본으로 1개 선택 가능, 따라서 ans는 1부터 시작
ans = 0
# 선택한 선분
selected = [False]*N
selected[0] = True
# idx = 선분의 개수, 인덱스
def sol(idx, cnt):
    if idx == N:
        return cnt

    # global ans
    for c in range(idx):
        if selected[c] and intersect(segments[c], segments[idx]):
            selected[idx] = False
            break
    if selected[idx]:
        cnt += 1
    
    max_cnt = sol(idx+1, cnt)
    if selected[idx]:
        selected[idx] = False
        max_cnt = max(max_cnt, sol(idx+1, cnt))
    else:
        selected[idx] = True
        max_cnt = max(max_cnt, sol(idx+1, cnt))
    
    return max_cnt

print(sol(0, 0))