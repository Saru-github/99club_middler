# 99club Day42_middler - 2024-09-01(Sun)
# https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms


class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        dp = [0]*len(nextVisit)
        for i in xrange(1, len(dp)):
            dp[i] = (dp[i-1]+1+(dp[i-1]-dp[nextVisit[i-1]])+1)%MOD
        return dp[-1]