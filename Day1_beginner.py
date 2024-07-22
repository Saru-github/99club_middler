# 99club Day1_beginner - 2024-07-22(Mon)
# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    return list(map(int, reversed(str(n))))


print(solution(12345))