import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(M)]
# 세로 위치(b)를 기준으로 오름차순 정렬
# lines.sort(lambda x:x[1])
turnable_locs = {}

for line in lines:
    # 만약 현재 line이 a에서 a번째 가로줄, 세로 위치는 b라면
    a, b = line
    # (a, b) 위치에서 이동할 수 있는 건 오른쪽으로 1칸 이동 후(a+1)
    # 아래로 한 칸 이동하는 것(b+1)
    turnable_locs[(a, b)] = (a+1, b+1)
    # 또는 (a+1, b) 위치였다면 왼쪽으로 한칸 이동 후(a+1-1) 아래로 한 칸 이동하는 것(b+1)
    turnable_locs[(a+1, b)] = (a, b+1)

# 최대로 내려갈 수 있는 세로 위치 max_b를 구한다.
# max_b = max(line[1] for line in lines)

# 현재 위치가 a번째 세로줄의 특정 위치에 있다면, 다음 이동해야 할 line을 탐색해서 turn한다.
# def turn(cur_loc):
#     # 만약 b 위치가 이미 max_b, 즉 마지막 위치보다 크다면
#     if cur_loc[1] > max_b:
#         return cur_loc

#     cur_a, cur_b = cur_loc
#     for line in lines:
#         # b의 위치가 일치해야 한다고 하자.
#         if line[0] == cur_a and line[1] == cur_b:
#             # 오른쪽으로 턴, 그리고 한 칸 아래로 내려온다.
#             cur_a += 1
#             cur_b += 1
#             break
#         elif line[0]+1 == cur_a and line[1] == cur_b:
#             # 왼쪽으로 턴, 그리고 한 칸 아래로 내려온다
#             cur_a -= 1
#             cur_b += 1
#             break
#         elif (line[0] ==cur_a or line[0]+1 == cur_a) and line[1] != 
#     return [cur_a, cur_b]


# def turn(cur_loc):
#     if cur_loc in turnable_locs:
#         return turnable_locs[cur_loc]
#     # 없다면, 아래로 한 칸 내려간다.
#     else:
#         cur_loc = (cur_loc[0], cur_loc[1]+1)
#         return cur_loc

# 한 명에 대해 사다리 타기를 실행한다.
# idx: 1~N
def climb_one(idx, turnable_locs):
    cur_loc = (idx, 1)

    # 만약 비어있다면:
    if not turnable_locs:
        return cur_loc[0]
    
    max_b = max(b for (a,b) in turnable_locs.keys()) - 1
    # while cur_loc[1] <= max_b:
    for _ in range(max_b):
        # cur_loc = turn(cur_loc)
        if cur_loc in turnable_locs:
            cur_loc = turnable_locs[cur_loc]
        # 없다면, 아래로 한 칸 내려간다.
        else:
            cur_loc = (cur_loc[0], cur_loc[1]+1)

    # 마지막에 idx번째 사람이 몇번째 가로줄에 있는지 확인한다.
    return cur_loc[0]

original_result = [climb_one(i, turnable_locs) for i in range(1, N+1)]
# print(f"original result: {original_result}")

# idx는 가로줄의 인덱스라고 하자.
def sol(idx, cnt, turnable_locs):
    if idx == 0:
        res = [climb_one(i, turnable_locs) for i in range(1, N+1)]
        if res == original_result:
            return cnt
        else:
            return -1
    
    cur_line = lines[idx-1]
    a, b = cur_line

    # 할 필요가 없다
    # sol(idx-1, cnt, turnable_locs)
    del turnable_locs[(a, b)]
    del turnable_locs[(a+1, b)]
    res = sol(idx-1, cnt-1, turnable_locs)
    # 현재 가로줄를 제거하고, 기존과 동일한 결과 출력이 가능한 경우
    if res >= 0:
        # cnt -= 1
        return res
    else:
        turnable_locs[(a, b)] = (a+1, b)
        turnable_locs[(a+1, b)] = (a, b)
        # 현재 가로줄를 제거하고, 기존과 동일한 결과 출력이 가능한 경우
        res = sol(idx-1, cnt, turnable_locs)
        if res >= 0:
            return min(cnt, res)
        else:
            return cnt

# cnt는 M부터 시작한다.
print(sol(6, 6, turnable_locs))