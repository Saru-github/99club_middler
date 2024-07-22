# 99club Day1 - 2024-07-22(Mon)
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

# n=1 [1] 1
# n=2 [1, 2],[2, 2]  1 2 2 2
# n=3 [1, 2, 3], [2, 2, 3], [3, 3, 3]
# n=4 [1, 2, 3, 4], [2, 2, 3, 4], [3, 3, 3, 4], [4, 4, 4, 4]
# left - right 사이의 숫자 i를 각 n 으로 나눈 나머지: 행, 몫: 열
# 행, 열중 최대값의 + 1를 한 값이 해당 i의 값이다.
# ex) n=4 , i=3 이면 4//3=0, 4%3=3, [0][3] 중 최대값에 +1 한 값이 그 배열의 수: 4

def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        row, col = i%n, i//n
        answer.append(max(row, col) + 1)

    return answer

print(solution(4, 5, 8))
