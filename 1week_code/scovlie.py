import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville)>=2:
        min_scoville1=heapq.heappop(scoville)
        if min_scoville1>=K:
            return answer
        else:
            min_scoville2 = heapq.heappop(scoville)
            heapq.heappush(scoville,min_scoville1+(min_scoville2*2))
            answer+=1


    if scoville[0]>=K:
        return answer
    else:
        return -1
scoville=[1, 2, 3, 9, 10, 12]
K=7
print(solution(scoville,K))