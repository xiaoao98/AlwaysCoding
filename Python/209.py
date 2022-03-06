class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # size = len(nums)
        # sum_nums = 0
        # min_len = size
        # for i in range(size):
        #     sum_nums += nums[i]
        # if sum_nums < s:
        #     return 0
        # if sum_nums == s:
        #     return size
        # pos1 = 0
        # pos2 = size - 1
        # while sum_nums >= s:
        #     if nums[pos1] < nums[pos2]:
        #         sum_nums -= nums[pos1]
        #         pos1 += 1
        #         min_len -= 1
        #     elif nums[pos1] > nums[pos2]:
        #         sum_nums -= nums[pos2]
        #         pos2 -= 1
        #         min_len -= 1
        #     elif nums[pos1] == nums[pos2]:
        #         pos1_tmp = pos1
        #         pos2_tmp = pos2
        #         while nums[pos1_tmp] == nums[pos2_tmp]:
        #             pos1_tmp += 1
        #             pos2_tmp -= 1
        #             if pos1_tmp>=pos2_tmp:
        #                 while sum_nums >= s:
        #                     sum_nums -= nums[pos1]
        #                     pos1 += 1
        #                     min_len -= 1
        #                 return min_len+1
        #         if nums[pos1_tmp] < nums[pos2_tmp]:
        #             sum_nums -= nums[pos1]
        #             pos1 += 1
        #             min_len -= 1
        #         elif nums[pos1_tmp] > nums[pos2_tmp]:
        #             sum_nums -= nums[pos2]
        #             pos2 -= 1
        #             min_len -= 1
        # return min_len+1
        size = len(nums)
        sum_nums = 0
        pos1 = 0
        min_len = size + 1
        for i in range(size):
            sum_nums += nums[i]
            while sum_nums >= s:
                min_len = min(min_len,i+1-pos1)
                sum_nums -= nums[pos1]
                pos1 += 1
        return min_len if min_len <= size else 0


if __name__ == "__main__":
    a = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    b = a.minSubArrayLen(s, nums)
    print(b)