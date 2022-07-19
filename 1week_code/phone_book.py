
import heapq
def solution(phone_book):
    heapq.heapify(phone_book)  
    p = heapq.heappop(phone_book)
    while phone_book:
        if p == phone_book[0][:len(p)]: 
            return False  
        p = heapq.heappop(phone_book)
        print(p)
    return True


pb1 = ["889", "12911", "8895524421"]
print(solution(pb1))