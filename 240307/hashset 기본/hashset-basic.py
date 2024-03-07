import sys
input = sys.stdin.readline

N = int(input())
my_set = set()
for _ in range(N):
    args = input().split()
    com = args[0]
    num = int(args[1])
    if com == 'add':
        my_set.add(num)
    elif com == 'remove':
        my_set.remove(num)
    # find
    else:
        if num in my_set:
            print("true")
        else:
            print("false")