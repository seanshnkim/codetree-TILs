import sys
input = sys.stdin.readline

N = int(input())
arrA = list(map(int, input().split()))
M = int(input())
arrB = list(map(int, input().split()))

setA = set(arrA)
for b in arrB:
    if b in setA:
        print(1)
    else:
        print(0)