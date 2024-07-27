# 99club beginner - 2024-07-27(Sat)
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    return min(len(nums) // 2, len(set(nums)))


print(solution([3, 3, 3, 2, 2, 4]))
