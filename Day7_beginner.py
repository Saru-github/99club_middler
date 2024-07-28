# 99club Day7_beginner - 2024-07-28(Sun)
# https://school.programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    answer = [arr[0]]
    tmp = answer[0]
    for i in arr:
        if tmp != i:
            answer.append(i)
            tmp = i
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
