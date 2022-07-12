
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    p_len=phone_book[0]
    tmp=len(p_len)
    i=1
    while i<=len(phone_book)-1:
        value=len(phone_book[i])-tmp+1
        for k in range(i,len(phone_book)):
            for j in range(0,value):
                if p_len==phone_book[k][j:tmp]:
                    answer=False
                    break
            if answer==False:
                break
        if answer==False:
            break
        p_len=phone_book[i]
        tmp=len(p_len)
        i+=1

    
    return answer



phone_book=["119", "97674223", "1195524421"]	
print(solution(phone_book))