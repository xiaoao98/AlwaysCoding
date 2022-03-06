class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for i in range(len(nums)):
            for per in list(output):
                for j in range(len(per)):
                    output.append(per[:j] + [nums[i]] + per[j:])
                per.append(nums[i])
        return output


if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3]
    b = a.permute(nums)
    print(b)