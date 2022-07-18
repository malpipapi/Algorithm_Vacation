def solution(prices):
    answer = []
    for k in range(len(prices)):
        tmp=0
        for i in range(k,len(prices)-1):
            if prices[k]<=prices[i]:
                tmp+=1
            else:
                break
        answer.append(tmp)
    return answer


prices=[1,2,3,2,3,1]

print(solution(prices))