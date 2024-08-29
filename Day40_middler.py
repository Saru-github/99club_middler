# 99club Day40_middler - 2024-08-30(Fri)
# https://leetcode.com/problems/unique-paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        v = []
        for i in range(m) :
            v.append([])
            for j in range(n) :
                v[i].append([])
        for i in range(m):
            for j in range(n):
                if i == 0 or j ==0 :
                    v[i][j] = 1
                else :
                    v[i][j] = v[i-1][j] + v[i][j-1]
        return v[m-1][n-1]