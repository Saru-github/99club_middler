# 99club Day24_middler - 2024-08-14(Wed)
# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    arr = [float("inf")] * 27

    for i, key in enumerate(keymap):
        for j, c in enumerate(key):
            idx = ord(c) - 65
            arr[idx] = min(arr[idx], j+1)
    print(arr)

    for target in targets:
        result = 0

        for c in target:
            idx = ord(c) - 65
            result += arr[idx]
        if result == float('inf'):
            answer.append(-1)
        else:
            answer.append(result)

    return answer
