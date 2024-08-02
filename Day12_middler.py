# 99club Day11_middler - 2024-08-02(Fri)
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    for i in range(n):
        if citations[i] > answer:
            answer = i + 1
        else:
            break

    return answer


print(solution([3, 0, 6, 1, 5]))