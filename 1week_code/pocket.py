import itertools

def solution(nums):
    result=len(set(nums))
    p_len=len(nums)//2
    answer=0
    if result < p_len:
        answer = result
    else:
        answer = p_len
    return answer



nums=[3,1,2,3,5]
print(solution(nums))

a = [
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
]
b = []
for i in a:
    b.append(i[0])
print(b)