class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for i in range(len(nums)):
            for per in list(output):
                per.append(nums[i])
            for per in list(output):
                for j in range(len(per)-1):
                    tmp = per[:j] + [nums[i]] + per[j:-1]
                    if tmp not in output:
                        output.append(tmp)
        return output


if __name__ == "__main__":
    a = Solution()
    nums = [2, 2, 1, 1]
    b = a.permuteUnique(nums)
    print(b)