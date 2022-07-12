import collections
def solution(participant, completion):

    a=set(participant)
    b=set(completion)
    answer=''
    if len(a)==len(b):
        result=dict(collections.Counter(participant))
        tmp=dict(collections.Counter(completion))
        for name in result:
            if(result[name]!=tmp[name]):
                answer=name
                break
    else:
        participant=sorted(participant)
        completion=sorted(completion)
        for i in range(len(participant)-1):
            if participant[i] != completion[i]:
                answer=participant[i]
                break
        if answer=='':
            answer=participant[-1]
    return answer




participant=["aa","ab","ac","ad","ae"]
completion=["ab","ae","ac","ad"]

print(solution(participant,completion))