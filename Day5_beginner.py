# 99club Day5_beginner - 2024-07-26(Fri)
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    # 두 배열 정렬
    participant.sort()
    completion.sort()

    # 두 배열을 묶어 같이 반복문을 돌림
    for a, b in zip(participant, completion):
        if a != b:
            return a
        else:
            continue

    # 반복문 안에서 다른 점이 발견되지 않으면, 배열의 가장 마지막 index 가 미완주자
    return participant[-1]


print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))