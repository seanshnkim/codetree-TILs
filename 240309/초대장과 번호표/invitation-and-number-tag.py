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

##### 디버깅 #####
# N, G = 20, 14
# groups = []
# groups.append(set([15, 17, 10, 1, 3, 11]))
# groups.append(set([1, 7]))
# groups.append(set([1, 11]))
# groups.append(set([1, 18]))
# groups.append(set([19, 14, 20, 6, 12, 1, 13, 7, 2, 10]))
# groups.append(set([5, 19, 4, 18, 11, 1, 12]))
# groups.append(set([12, 5]))
# groups.append(set([3, 18, 7, 13, 6]))
# groups.append(set([5, 1]))
# groups.append(set([4, 5]))
# groups.append(set([12, 13]))
# groups.append(set([12, 7, 3]))
# groups.append(set([7, 9]))
# groups.append(set([20, 5, 3]))

# 1번은 초대장을 무조건 준다
ans = 1

# 초대받은 사람을 한 명씩 설정하면서 for loop을 실행
# 처음에는 1번 사람이 초대된 것이므로, 1번을 invited에 저장
invited_people = deque([1])

while invited_people:
    invited = invited_people.pop()
    for group_set in groups:
        if not group_set:
            continue
        # discard method를 쓰면, 해당 set에 원소가 존재하지 않아도 에러 X
        group_set.discard(invited)
        
        # 만약 초대받은 사람을 제외한 사람이 그룹에 1명밖에 없다면, 그 사람을 다음 초대받은 사람으로 설정
        if len(group_set) == 1:
            left_item = group_set.pop()
            invited_people.appendleft(left_item)
            # print(invited_people)
            ans += 1
        
        # 만약 그룹에 이제 남은 사람이 없다면, 그룹을 삭제
        # if not group_set:
        #     groups.remove(group_set)
        
print(ans)