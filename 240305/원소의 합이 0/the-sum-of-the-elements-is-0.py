import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
nums3 = list(map(int, input().split()))
nums4 = list(map(int, input().split()))

count1 = defaultdict(int)
count2 = defaultdict(int)
# for n1, n2 in zip(nums1, nums2):
for n1 in nums1:
    for n2 in nums2:
        count1[n1+n2] += 1
# for n3, n4 in zip(nums3, nums4):
for n3 in nums3:
    for n4 in nums4:
        count2[n3+n4] += 1
        
ans = 0
for sum1 in count1:
    if -sum1 in count2:
        ans += count1[sum1] * count2[-sum1]
print(ans)