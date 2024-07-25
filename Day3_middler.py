# 99club Day3_middler - 2024-07-24(Wed)
# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):

    # answer = sorted(strings, key=lambda x: (x[n], x))

    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    return [strings[i][1:] for i in range(len(strings))]


print(solution(["sun", "bed", "car"], 1))