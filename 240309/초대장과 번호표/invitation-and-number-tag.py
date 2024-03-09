import sys
input = sys.stdin.readline
from collections import deque

N, G = map(int, input().split())
groups = []
group_sizes = []
for _ in range(G):
    group = list(map(int, input().split()))
    # 0번째 원소는 그룹의 크기
    group_size, group_set = group[0], set(group[1:])
    groups.append(group_set)
    group_sizes.append(group_size)

# 1번은 초대장을 무조건 준다
ans = 1

# 초대받은 사람을 한 명씩 설정하면서 for loop을 실행
# 처음에는 1번 사람이 초대된 것이므로, 1번을 invited에 저장
invited_people = deque([1])

# 반복
# for ... :
while invited_people:
    invited = invited_people.pop()
    for group_set in groups:
        # discard method를 쓰면, 해당 set에 원소가 존재하지 않아도 에러 X
        group_set.discard(invited)
        
        # 만약 초대받은 사람을 제외한 사람이 그룹에 1명밖에 없다면, 그 사람을 다음 초대받은 사람으로 설정
        if len(group_set) == 1:
            invited_people.appendleft(group_set.pop())
            ans += 1
        
        # 만약 그룹에 이제 남은 사람이 없다면, 그룹을 삭제
        if not group_set:
            groups.remove(group_set)
        
print(ans)