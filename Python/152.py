class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]

        def productnum(nums, low, high):
            if low == high:
                return nums[low]
            product = 1
            for i in range(low, high):
                product = product * nums[i]
            return product

        largest = 0
        place0 = 0
        flag = 1
        counter = 0

        for i in range(len(nums)):
            if nums[i] < 0:
                if flag:
                    placehead = i
                    flag = 0
                    counter = 1
                    placetail = i
                else:
                    placetail = i
                    counter = 1 - counter
            if nums[i] == 0 or i == len(nums) - 1:
                if i == len(nums) - 1:
                    tmpi = i + 1
                else:
                    tmpi = i
                if counter == 0:
                    largest = max(largest, productnum(nums, place0, tmpi))
                if counter == 1:
                    if placehead == tmpi - 1:
                        largest = max(largest, productnum(nums, place0, placehead))
                    else:
                        largest = max(largest, productnum(nums, place0, placetail),
                                      productnum(nums, placehead + 1, tmpi))
                flag = 1
                counter = 0
                place0 = tmpi + 1
        return largest


if __name__ == "__main__":
    a = Solution()
    nums = [-3, 0, 1, -2]
    b = a.maxProduct(nums)
    print(b)