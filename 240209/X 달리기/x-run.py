import sys
import math
input = sys.stdin.readline

X = int(input())

# max 속도(그러나 잠정값)를 의미하는 m
# int() -> 내림이기 때문에 항상 m^2은 X보다 작거나 같게 된다.
m = int(math.sqrt(X))

if m*m == X:
    ans = 2*m - 1
else:
    if m*m + m >= X:
        ans = 2*m
    else:
        ans = 2*m + 1

print(ans)