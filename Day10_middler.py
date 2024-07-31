# 99club Day10_middler - 2024-07-31(Wed)
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    for i in operations:
        o, n = i.split()

        if o == "I":
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))

        if len(min_heap) != 0:
            if o == "D" and n == "1":
                max = -heapq.heappop(max_heap)
                min_heap.remove(max)
                heapq.heapify(min_heap)
            elif o == "D" and n == "-1":
                min = heapq.heappop(min_heap)
                max_heap.remove(-min)
                heapq.heapify(max_heap)

    if len(max_heap) == 0:
        return [0,0]
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))