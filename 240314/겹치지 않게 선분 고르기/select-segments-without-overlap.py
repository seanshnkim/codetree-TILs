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
selected = [True]*N
# cnt = 선분의 개수, 인덱스
def sol(cnt):
    if cnt == N:
        return

    global ans
    for c in range(cnt):
        if selected[c] and intersect(segments[c], segments[cnt]):
            selected[cnt] = False
            break
    if selected[cnt]:
        ans += 1
    
    sol(cnt+1)

sol(0)
print(ans)