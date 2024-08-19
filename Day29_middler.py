# 99club Day28_middler - 2024-08-19(Mon)
# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums):
        N = len(nums)
        ans = [1] * N

        for i in range(1, N):
            maxi = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, ans[j])

            ans[i] = maxi + 1

        return max(ans)