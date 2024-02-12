import sys
input = sys.stdin.readline

N = int(input())
S = input()
seats = [seat for seat in S]

# 목표: 가장 가까운 두 사람 간의 거리를 최대로 한다.
# 최소 거리를 찾되, 최소 거리보다 큰 거리에 대해 가운데로 나눠보고
# 나눈 결과 생기는 두 거리(A, B) 중에 기존 최소 거리보다 작은 게 있으면 그걸 답으로 반환한다.
# 만약 A,B 중 기존 최소 거리보다 작은 게 없다면 기존 최소 거리를 답으로 반환한다.
# print(seats)
# 하지만 최소 거리보다 간격이 큰 모든 경우에 대해 해볼 필요는 없고
# 최대 거리일 때만 해보면 된다.

min_dist = N-1
max_dist, cur_dist = 1, 1

# STEP 1: 최소, 최대 거리를 찾는다.
for s in range(N):
    seat = seats[s]
    if seat == '0':
        cur_dist += 1
    else:
        if s == 0:
            continue
        max_dist = max(max_dist, cur_dist)
        min_dist = min(min_dist, cur_dist)
        cur_dist = 1

# STEP 2: 최대 거리를 찾았다면, 가운데에 사람을 배치해서 생기는
# 두 거리 A, B 중 더 작은 것(max_dist // 2)을 기존 최소 거리와 비교한다.
# 어쨌든 가장 가까운 두 사람의 거리를 구하는 거니까 min을 써야 한다.
# 단, 최대 거리를 가운데로 나누는 알고리즘이 거리를 최대화하는 것이라고 볼 수 있다.
# print(max_dist, min_dist)
ans = min((max_dist // 2), min_dist)

print(ans)