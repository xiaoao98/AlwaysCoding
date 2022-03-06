class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        size = len(triangle)
        dp = [0] * size
        dp[0] = triangle[0][0]
        for i in range(1, size):
            for j in range(i+1):
                if j == 0:
                    tmp = dp[j]
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = tmp + triangle[i][j]
                else:
                    tmp, dp[j] = dp[j], min(tmp, dp[j]) + triangle[i][j]
        return min(dp)


if __name__ == "__main__":
    a = Solution()
    nums = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    b = a.minimumTotal(nums)
    print(b)