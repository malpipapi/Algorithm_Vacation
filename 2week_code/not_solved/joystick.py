def solution(name):
    answer = 0
    tmp=""
    for i in range(len(name)):
        tmp+="A"
    i=0
    count=0
    j=0
    while tmp!=name:
        a=chr(ord(tmp[i]))
        b=chr(ord(name[i]))
        while a!=b:
            if i==0:
                a=chr(ord(tmp[i])+1)
                tmp=a+tmp[i+1:]
                count+=1
            else:
                print(tmp)
                a=chr(ord(tmp[i])+1)
                tmp=tmp[:j+1]+a+tmp[i+1:]
                if a==b:
                    j+=1
                    count+=1
        print(tmp)
        i+=1
    return count


name="JAN"
print(solution(name))
