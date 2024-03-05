import sys
input = sys.stdin.readline

N = int(input())
_dict = {}
for i in range(N):
    input_str = input().rstrip('\n')
    if input_str in _dict:
        _dict[input_str] += 1
    else:
        _dict[input_str] = 1

print(max(_dict.values()))