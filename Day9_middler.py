# 99club Day8_middler - 2024-07-30(Tue)
#https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    spicy = heapq.heappop(scoville)
    while spicy < K:
        try:
            new_spicy = spicy + (heapq.heappop(scoville) * 2)
        except:
            return -1
        heapq.heappush(scoville,new_spicy)
        spicy = heapq.heappop(scoville)
        answer += 1


    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))