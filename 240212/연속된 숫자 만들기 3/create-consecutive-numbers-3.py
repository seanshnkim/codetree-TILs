import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
dist_left, dist_right = nums[1] - nums[0], nums[2] - nums[1]
ans = 0
# Case 1: 둘다 거리가 1이면, 바로 종료
if dist_left == 1 and dist_right == 1:
    ans = 0
# Case 2: 둘 중에 하나만 거리가 1이면
elif dist_left == 1:
    ans = dist_right - 1
elif dist_right == 1:
    ans = dist_left - 1
# Case 3: 둘 다 거리가 1보다 크면,
else:
    ans = max(dist_left, dist_right) - 1
print(ans)