# 99club Day11_middler - 2024-08-01(Thu)
# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 or cards2:
            if cards1 and word == cards1[0]:
                cards1.remove(word)
            elif cards2 and word == cards2[0]:
                cards2.remove(word)
            else:
                return "No"
    return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))