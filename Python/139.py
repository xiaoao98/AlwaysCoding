class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dic = set()
        dp = [-1]
        size = len(s)
        for word in wordDict:
            dic.add(word)
        for i in range(size):
            size_dp = len(dp)
            for j in range(size_dp):
                if s[(dp[j]+1):(i+1)] in dic:
                    if i not in dp:
                        dp.append(i)
        if dp[-1] == size - 1:
            return True
        else:
            return False


if __name__ == "__main__":
    a = Solution()
    print(a.wordBreak("leetcode", ["leet", "code"]))