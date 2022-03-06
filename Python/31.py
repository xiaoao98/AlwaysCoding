class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i = size - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            nums[:] = nums[::-1]
            return
        j = i
        while j < len(nums) and nums[j] > nums[i - 1]:
            j += 1
        nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]
        nums[:] = nums[:i] + nums[i:][::-1]


if __name__ == "__main__":
    a = Solution()
    nums = [1, 3, 2]
    b = a.nextPermutation(nums)
    print(nums)