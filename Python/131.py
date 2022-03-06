class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dps = []
        dps.append([s[0]])
        size = len(s)
        for i in range(1, size):
            size_dps = len(dps)
            for j in range(size_dps):
                dp = dps[j]
                if dp[-1] == s[i]:
                    dp_new = dp[:-2]
                    dp_new.append(dp[-1]+s[i])
                    dps.append(dp_new)
                if len(dp)>=2 and dp[-2] == s[i]:
                    dp_new = dp[:-3]
                    dp_new.append(s[i]+dp[-1]+s[i])
                    dps.append(dp_new)
                dp.append(s[i])
        return dps


if __name__ == "__main__":
    a = Solution()
    print(a.partition("cdd"))

