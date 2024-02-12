import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
inputs = [tuple(map(int, input().split())) for _ in range(N)]

# CASE 1: 1 = 가위 /  2 = 바위 / 3 = 보
# CASE 2: 1 = 가위 /  2 = 보 / 3 = 바위
# CASE 3: 1 = 바위 /  2 = 가위 / 3 = 보
# CASE 4: 1 = 바위 /  2 = 보 / 3 = 가위
# CASE 5: 1 = 보 /  2 = 가위 / 3 = 바위
# CASE 6: 1 = 보 /  2 = 바위 / 3 = 가위

answers = []
# CASE 1: 1 = 가위 /  2 = 바위 / 3 = 보
# cnt = 0
# for first, second in inputs:
#     if (first == 1 and second == 3) \
#     or (first == 2 and second == 1) \
#     or (first == 3 and second == 2):
#         cnt += 1
# answers.append(cnt)

for perm in permutations((1,2,3)):
    cnt = 0
    for first, second in inputs:
        if (first == perm[0] and second == perm[2]) \
        or (first == perm[1] and second == perm[0]) \
        or (first == perm[2] and second == perm[1]):
            cnt += 1
    answers.append(cnt)
print(max(answers))