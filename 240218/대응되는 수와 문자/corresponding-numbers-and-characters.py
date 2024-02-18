import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d1 = {}
d2 = {}
for i in range(N):
    cur_input = input().rstrip('\n')
    d1[cur_input] = i+1
    d2[i+1] = cur_input
for _ in range(M):
    cur_input = input().rstrip('\n')
    if cur_input in d1:
        print(d1[cur_input])
    else:
        print(d2[int(cur_input)])