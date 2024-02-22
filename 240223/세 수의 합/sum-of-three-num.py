import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

# for i in range(N):
#     K_diff = K - nums[i]
#     for j in range(i+1, N):
#         for l in range(j+1, N):
#             if nums[j] + nums[l] == K_diff:
#                 ans += 1

count = defaultdict(int)
for n in nums:
    count[n] += 1

for i in range(N):
    K_diff = K - nums[i]
    count[nums[i]] -= 1

    for j in range(i+1, N):
        count[nums[j]] -= 1
        diff = K_diff - nums[j]
        ans += count[diff]

    for j in range(i+1, N):
        count[nums[j]] += 1

print(ans)