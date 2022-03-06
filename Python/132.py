class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dps = []
        dps.append([0, s[0]])
        size = len(s)
        for i in range(1, size):
            size_dps = len(dps)
            for j in range(size_dps):
                dp = dps[j]
                if dp[-1] == s[i]:
                    dps.append(dp[:-1]+[dp[-1]+s[i]])
                if len(dp)>=2 and dp[-2] == s[i]:
                    dps.append(dp[:-2]+[s[i]+dp[-1]+s[i]])
                    dps[-1][0] -= 1
                dp[0] += 1
        output = size - 1
        for dp in dps:
            output = min(output, dp[0])
        return output

if __name__ == "__main__":
    a = Solution()
    print(a.minCut("cdd"))