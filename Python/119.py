class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        outputarray = [1, 1]
        for i in range(1, rowIndex):
            for j in range(len(outputarray) - 1, 0, -1):
                outputarray[j] = outputarray[j] + outputarray[j - 1]
            outputarray.append(1)
        return outputarray


if __name__ == "__main__":
    a = Solution()
    num = 3
    nums = a.getRow(num)
    for i in range(len(nums)):
        print(nums[i])
    # i = 0
    # while i > 5:
    #     print(i)
    #     i+=1
    # else:
    #     print(i+5)

