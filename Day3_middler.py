# 99club Day2_beginner - 2024-07-24(Wed)
# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):

    # answer = sorted(strings, key=lambda x: (x[n], x))

    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer


print(solution(["sun", "bed", "car"], 1))