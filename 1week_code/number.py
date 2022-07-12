def solution(arr):
    answer = []
    tmp=0
    i=0
    answer.append(arr[0])
    while len(arr)>0: 
        if arr[0]==answer[tmp]:
            arr.pop(0)
        else:
            answer.append(arr[0])
            arr.pop(0)
            tmp+=1
        

    
    return answer

arr=[1,1,3,3,0,1,1]
print(solution(arr))