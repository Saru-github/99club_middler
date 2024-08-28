# 99club Day38_middler - 2024-08-28(Wed)
# https://school.programmers.co.kr/learn/courses/30/lessons/142085


from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heappush(h, e)
        if len(h) > k:
            n -= heappop(h)
        if n < 0:
            return i

    return len(enemy)
