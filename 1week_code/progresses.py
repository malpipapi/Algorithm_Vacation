def solution(progresses, speeds):
    answer=[]
    tmp=[]
    k=0
    for i in range(len(progresses)):
        i_value=0

        while progresses[i]<100:
            progresses[i]+=speeds[i]
            i_value+=1

        if not tmp:
            tmp.append(i_value)
            k+=1
        else:
            if i_value>tmp[0]:
                answer.append(k)
                tmp=[]
                tmp.append(i_value)
                k=1
            else:
                tmp.append(k)
                k+=1
    if tmp:
        answer.append(k)
                
        

    return answer


progresses=[40, 93, 30, 55, 60, 65]
speeds=[60, 1, 30, 5 , 10, 7]
print(solution(progresses,speeds))