from audioop import reverse
import re


def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]==reserve[j]:
                reserve[j]=-5
                n-=1
                answer+=1
                lost[i]=-1
    m=0
    while m<len(lost):
        for k in range(len(reserve)):
            if reserve[k]==0:
                break
            if reserve[k]==lost[m]-1:
                reserve[k]=-10
                n-=1
                lost[m]=-1
                answer+=1
                break
            elif reserve[k]==lost[m]+1:
                reserve[k]=-10
                lost[m]=-1
                n-=1
                answer+=1
                break
        m+=1
    for a in range(len(reserve)):
        
        if reserve[a]==-10:
            print(reserve[a])
            answer+=1
            n-=1
        elif reserve[a]>0:
            print(reserve[a])
            answer+=1
            n-=1
    for z in range(len(lost)):
        if lost[z]!=-1:
            n-=1
    if n>0:
        answer+=n
    return answer




n=30
lost= [1, 2, 7, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27]
reserve=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 24, 25, 26, 27, 28]
print(solution(n,lost,reserve))