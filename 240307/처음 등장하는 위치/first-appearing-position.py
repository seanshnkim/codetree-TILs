import sys
input = sys.stdin.readline
from sortedcontainers import SortedDict

N = int(input())
nums = list(map(int, input().split()))

sd = SortedDict()
for i in range(N):
    num = nums[i]
    if num not in sd:
        sd[num] = i+1

for num, order in sd.items():
    print(num, order)