from collections import Counter, defaultdict
def solution(clothes):
    answer = 1
    clotheslist = defaultdict(int)
    for n,t in clothes:
        clotheslist[t] += 1
    for t in clotheslist:
        answer*=clotheslist[t]+1
    answer-=1
    return answer


clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))