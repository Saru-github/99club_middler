# 99club Day19_middler - 2024-08-09(Fri)
# https://school.programmers.co.kr/learn/courses/30/lessons/42883


def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1

    return answer
