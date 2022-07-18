def solution(arr):
    answer = []
    tmp=0
    answer.append(arr[0])
    for i in range(len(arr)):
        if arr[i]!=answer[tmp]:
            answer.append(arr[i])
            tmp+=1
    return answer

arr=[1,1,3,3,0,1,1]
print(solution(arr))