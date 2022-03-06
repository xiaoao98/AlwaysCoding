class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        output = []

        def helper(matrix, r1, r2, c1, c2, output):
            # r = len(matrix)
            # c = len(matrix[0])
            if r1 > r2 or c1 > c2:
                return
            if r1 == r2:
                output += matrix[r1][c1:c2 + 1]
                return
            if c1 == c2:
                for i in range(r1, r2+1):
                    output.append(matrix[i][c1])
                return
            else:
                output += matrix[r1][c1:c2]
                for i in range(r1, r2):
                    output.append(matrix[i][c2])
                output += matrix[r2][c1 + 1:c2 + 1][::-1]
                for i in range(r2, r1, -1):
                    output.append(matrix[i][c1])
                helper(matrix, r1 + 1, r2 - 1, c1 + 1, c2 - 1, output)

        helper(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, output)
        return output


if __name__ == '__main__':
    a = Solution()
    b = a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(b)
