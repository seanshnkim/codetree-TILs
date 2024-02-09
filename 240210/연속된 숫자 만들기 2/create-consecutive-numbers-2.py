import sys
input = sys.stdin.readline
# 처음에 문제를 너무 어렵게 해석했고, while 문으로 돌려서 계속 반복해서 찾아나가야 한다고 생각했다.
# 하지만 그게 아니라 답은 몇 가지로 이미 정해져있는 쉬운 문제였다 -> 종이 위에 열심히 케이스별로 나눠서 어떻게 상황이 전개되는지 깊게 생각하지 않았기 때문
nums = list(map(int, input().split()))
d_left  = nums[1] - nums[0]
d_right = nums[2] - nums[1]

ans = 0

if d_left == 1 and d_right == 1:
    ans = 0
elif d_left == 2 or d_right == 2:
    ans = 1
else:
    ans = 2

print(ans)