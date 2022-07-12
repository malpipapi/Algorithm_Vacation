def solution(s):
    answer = True
    arr=[]
    if s[0]==")":
        return False
    else:
        arr.append(s[0])
    tmp=0
    for i in range(len(s)):
        if tmp==-1 and s[i]!=")":
            return False
        if s[i]==arr[tmp]:
            arr.append(s[i])
            tmp+=1
        elif s[i]!=arr[tmp]:
            arr.pop()
            tmp-=1

    if len(arr)>1:
        return False
    return True
        


s="(()("


print(solution(s))