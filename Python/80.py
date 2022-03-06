class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        rlen = len(nums)
        i = 0
        while i < rlen-1:
            if nums[i + 1] == nums[i]:
                counter += 1
                if counter > 2:
                    for j in range(i + 1, rlen - 1):
                        nums[j] = nums[j + 1]
                    rlen = rlen - 1
                    counter = counter - 1
                    i-=1
            else:
                counter = 1
            i += 1
        return rlen


if __name__ == "__main__":
    a = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    rlen = a.removeDuplicates(nums)
    for i in range(rlen):
        print(nums[i])
