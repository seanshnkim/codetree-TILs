import sys
input = sys.stdin.readline

N = int(input())
_dict = {}
for _ in range(N):
    args = input().split()
    if args[0] == "add":
        _dict[args[1]] = args[2]
    elif args[0] == "remove":
        del _dict[args[1]]
    else:
        if args[1] in _dict:
            print(_dict[args[1]])
        else:
            print(None)