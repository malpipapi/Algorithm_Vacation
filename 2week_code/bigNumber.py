from itertools import combinations
def solution(number, k):
    
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
            if len(answer)==n:
                    break
            if not answer or k<=0:
                break
        if len(answer)==n:
                break
        answer.append(num)
    tmp=""
    for i in range(len(answer)):
        tmp+=answer[i]

            


    return tmp

number="4321"
k=1
print(solution(number,k))