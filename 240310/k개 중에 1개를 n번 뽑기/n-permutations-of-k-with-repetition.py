import sys
input = sys.stdin.readline

K, N = map(int, input().split())
answer = []

def repeat(curr_num, digit):
    answer.append(curr_num)

    if digit == 0:
        print(*answer)
        answer.pop()
        return
    
    for k in range(1, K+1):
        repeat(k, digit-1)
    
    answer.pop()
    
    return 


for k in range(1, K+1):
    repeat(k, N-1)