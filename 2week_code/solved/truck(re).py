def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    
    while True :
        if len(truck_weights) == 0 and sum(bridge) == 0:
            break
            
        answer += 1
        del bridge[0]
        print(bridge)
        nextNum = 0
        
        if truck_weights: 
            if sum(bridge) + truck_weights[0] <= weight:
                nextNum = truck_weights[0]
                del truck_weights[0]
        bridge.append(nextNum)
        print(bridge)
        
    return answer

bridge_length=2
weight=10
truck_weights=[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))