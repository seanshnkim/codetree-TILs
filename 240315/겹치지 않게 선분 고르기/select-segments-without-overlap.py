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
# selected = [False]*N
selected = [True]*N
# selected[0] = True
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
        # idx번째 선분이 겹치지 않는다면, idx번째 선분을 선택하고 다음 선분들을 조합하는 경우와
        max_cnt = sol(idx+1, cnt+1)
        selected[idx] = False
        # idx번째 선분을 선택하지 않고 다음 선분들을 조합하는 경우를 비교한다.
        # -> 아니 근데 이걸 비교해야돼? 그냥 idx번째 선분은 선택하면 되지 않나?
        max_cnt = max(max_cnt, sol(idx+1, cnt))
        
    else:
        # idx번째 선분이 0...idx-1번째 선분 중 최소 하나와 겹쳐서 선택할 수 없다면,
        # idx번째 선분을 선택하지 않고 cnt를 업데이트
        max_cnt = sol(idx+1, cnt)
        # selected[idx] = True # -> 현재 선택할 수 없는데 왜 True 값으로 만드느냐!
        # max_cnt = max(max_cnt, sol(idx+1, cnt))
    selected[idx] = True
    
    return max_cnt

print(sol(0, 0))