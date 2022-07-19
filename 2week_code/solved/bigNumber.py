from itertools import combinations
def solution(number, k):
    tmp=""
    answer=[]
    n=len(number)-k
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k >0:
            while answer[-1]<num:
                answer.pop()
                k-=1
                if not answer or k<=0:
                    break
        answer.append(num)
        if len(answer)==n:
            break
    for i in range(len(answer)):
        tmp+=answer[i]
    return tmp

number="4321"
k=1
print(solution(number,k))