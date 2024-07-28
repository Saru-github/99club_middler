# 99club Day7_middler - 2024-07-28(Sun)
# https://school.programmers.co.kr/learn/courses/30/lessons/12946


def solution(n):
    def hanoi(start, target, temp, N):
        if N == 1:
            return [[start, target]]
        return hanoi(start, temp, target, N-1) + [[start, target]] + hanoi(temp, target, start, N-1)

    return hanoi(1, 3, 2, n)


print(solution(2))
