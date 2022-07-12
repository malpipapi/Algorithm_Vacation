from collections import deque

def solution(priorities, location):
    a=priorities[0]
    answer = 0
    for i in range(len(priorities)):
        max_number=max(priorities)
        for j in range(len(priorities)):
            if max_number==priorities[i]:
                answer+=1
                priorities[i]=0
                max_number=max(priorities)
                if i==location:
                    return answer
priorities=[1, 1, 9, 1, 1, 1]
location=0
print(solution(priorities,location))