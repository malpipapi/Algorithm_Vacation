from collections import deque

def solution(people, limit):
    people.sort()
    deq= deque(people)
    count=0
    while deq:
        nowBoatWeight=deq.pop()
        count+=1
        if len(deq)==0:
            break
        if (nowBoatWeight+deq[0])<=limit:
            deq.popleft()
            continue
        if (nowBoatWeight+deq[-1])<=limit:
            deq.pop()
        print(deq)
    return count
        



people=[1,1,1,1,1,1]
limit=240

print(solution(people,limit))