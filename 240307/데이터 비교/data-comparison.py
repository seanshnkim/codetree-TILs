import sys
input = sys.stdin.readline

N = int(input())
nums1 = list(map(int, input().split()))
M = int(input())
nums2 = list(map(int, input().split()))

s1 = set(nums1)
ans = []
for n2 in nums2:
    if n2 in s1:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)