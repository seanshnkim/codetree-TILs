import sys
input = sys.stdin.readline

N = int(input())
nums_before = list(map(int, input().split()))
nums_after = list(map(int, input().split()))
cnt = 0

for i in range(N-1):
    diff = nums_before[i] - nums_after[i]
    nums_before[i+1] += diff
    cnt += diff

print(cnt)


'''
1번 집에 있는 2명은 2~4번 어디론가 가야한다. -> 2번으로 보낸다.
-> 2번 집은 6명이 된다.

2번 집에 있는 2+2명은 3~4번 어디론가 가야한다.
-> 3번으로 보낸다.
-> 3번 집은 7명이 된다.

3번 집에 있는 4명은 4번 집으로 간다.

이렇게 하면 2*1 + 4*1 + 4*1 = 10이 된다.
'''