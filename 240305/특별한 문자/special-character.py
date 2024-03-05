import sys
input = sys.stdin.readline

input_str = input().rstrip('\n')
count = {}

for cur_char in input_str:
    if cur_char not in count:
        count[cur_char] = 1
    else:
        count[cur_char] += 1

ans = None
for cur_char in input_str:
    if count[cur_char] == 1:
        ans = cur_char
        break
print(ans)