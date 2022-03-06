class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        def helper(matrix, target, low_row, low_col, high_row, high_col):
            if(low_row > high_row or low_col > high_col):
                return False
            mid_row = (low_row + high_row)//2
            mid_col = (low_col + high_col)//2
            if matrix[mid_row][mid_col] == target:
                return True
            if matrix[mid_row][mid_col] > target:
                return helper(matrix, target, low_row, low_col, high_row, mid_col-1) or \
            helper(matrix, target, low_row, mid_col, mid_row-1, high_col)
            if matrix[mid_row][mid_col] < target:
                return helper(matrix, target, mid_row+1, low_col, high_row,high_col) or \
            helper(matrix, target, low_row, mid_col+1, mid_row, high_col)
        return helper(matrix, target, 0, 0, len(matrix)-1, len(matrix[0])-1)


if __name__ == "__main__":
    a = Solution()
    nums = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    target = 20
    b = a.searchMatrix(nums, target)
    print(b)