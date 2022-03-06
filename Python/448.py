class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # returnlist = [i for i in range(1, len(nums) + 1)]
        # for i in range(len(nums)):
        #     if nums[i] == returnlist[nums[i] - 1]:
        #         returnlist[nums[i] - 1] = 0
        # # while 0 in returnlist:
        # #     returnlist.remove(0)
        # pos = point = rlen = 0
        # while point < len(returnlist):
        #     if returnlist[point] != 0:
        #         returnlist[pos] = returnlist[point]
        #         rlen += 1
        #         pos += 1
        #     point += 1
        # return returnlist[0:rlen]
        i = len(nums)
        nums.append(0)
        while i > 0:
            if i == nums[i] or nums[i] == nums[nums[i]]:
                i -= 1
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return [i for i, n in enumerate(nums) if i != n]


if __name__ == "__main__":
    a = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    output = a.findDisappearedNumbers(nums)
    for i in range(len(output)):
        print(output[i])