import sys
input = sys.stdin.readline

# 무조건 세 사람
# 양 끝쪽에 있는 사람 중 한 명이어야 함
# 예시 데이터:
'''
2 11 14
-> 2를 11과 14 사이로 옮긴다. 왜? 11과 14 사이 거리가 더 짧기 때문

11 13 14
-> 14를 12로 옮긴다. 11 12 13
'''
nums = list(map(int, input().split()))
d_left  = nums[1] - nums[0]
d_right = nums[2] - nums[1]

cnt = 0

# while True:
while True:
    # 만약 왼쪽 간격이 오른쪽 간격보다 작다면, 
    # 맨 오른쪽 사람을 0번째와 1번째 사이로 옮긴다.

    if d_left == 1 and d_right == 1:
        break

    elif d_left == 1 and d_right > 1:
        prev_num1 = nums[1]
        nums[1] = (prev_num1 + nums[2]) // 2
        nums[0] = prev_num1
        # cnt += 1
        
    elif d_right == 1 and d_left > 1:
        prev_num1 = nums[1]
        nums[1] = (nums[0] + prev_num1) // 2
        nums[2] = prev_num1
        # cnt += 1

    else:
        if d_left > d_right:
            prev_num1 = nums[1]
            nums[1] = (prev_num1 + nums[2]) // 2
            nums[0] = prev_num1
            # cnt += 1
        else:    
            prev_num1 = nums[1]
            nums[1] = (nums[0] + prev_num1) // 2
            nums[2] = prev_num1
            # cnt += 1

    d_left  = nums[1] - nums[0]
    d_right = nums[2] - nums[1]
    cnt += 1

print(cnt)