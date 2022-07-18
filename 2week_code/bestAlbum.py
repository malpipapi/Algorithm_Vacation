from collections import defaultdict

def solution(genres, plays):
    answer = []
    ex=set(genres)
    tmp=tuple(ex)
    b=len(tmp)
    value=[]
    key=[]
    for i in range(b):
        for j in range(len(genres)):
            if tmp[i]==genres[j]:
                value.append(j)
        key.append(value)
        value=[]
    

    return key
    




genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

print(solution(genres,plays))

 #counter = defaultdict(int)
    #fo#r n,letter in genres:
     #   counter[letter] += 1
    #return counter