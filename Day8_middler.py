# 99club Day8_middler - 2024-07-29(Mon)
# https://school.programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    result = []

    # len(progresses) != 0 과 같은 의미 (배열에 값이 있기때문에 True 가 나온다)
    while progresses:

        # 각 작업의 1일씩 진도 업데이트
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed

        # 배포할 작업 개수
        count = 0

        # 맨 앞 작업 진도가 100% 이상되면, progresses와 speeds 리스트에서 해당 작업 제거하고 작업 수 증가
        # progresses가 빈 배열이 아닐 땐 True 반환, 빈 배열일 땐 False 반환
        while progresses and progresses[0] >= 100:
            del progresses[0], speeds[0]
            count += 1

        if count > 0:
            result.append(count)

    return result


print(solution([93, 30, 55], [1, 30, 5]))
