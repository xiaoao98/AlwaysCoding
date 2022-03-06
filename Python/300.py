class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy = {}
        size = len(nums)
        output = size
        for index, value in enumerate(nums):
            copy[value] = index
        nums.sort()
        for i in range(size-1):
            if copy[nums[i+1]] <= copy[nums[i]]:
                output -= 1
        return output


if __name__ == "__main__":
    a = Solution()
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    b = a.lengthOfLIS(nums)
    print(b)