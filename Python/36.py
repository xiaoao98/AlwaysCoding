class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic = {}

        for i in range(9):
            for j in range(9):
                dic[str(j + 1)] = 1
            for j in range(9):
                if board[i][j] not in dic and board[i][j] != '.':
                    return False
                if board[i][j] in dic and dic[board[i][j]] == 0:
                    return False
                if board[i][j] in dic and dic[board[i][j]] == 1:
                    dic[board[i][j]] = 0

        for j in range(9):
            for i in range(9):
                dic[str(i + 1)] = 1
            for i in range(9):
                if board[i][j] not in dic and board[i][j] != '.':
                    return False
                if board[i][j] in dic and dic[board[i][j]] == 0:
                    return False
                if board[i][j] in dic and dic[board[i][j]] == 1:
                    dic[board[i][j]] = 0

        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        mediums = [[1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7], [7, 1], [7, 4], [7, 7]]
        for medium in mediums:
            for i in range(9):
                dic[str(i + 1)] = 1
            for neighbor in neighbors:
                row = medium[0] + neighbor[0]
                col = medium[1] + neighbor[1]
                if board[row][col] in dic and dic[board[row][col]] == 0:
                    return False
                if board[row][col] in dic and dic[board[row][col]] == 1:
                    dic[board[row][col]] = 0
        return True


if __name__ == "__main__":
    a = Solution()
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    b = a.isValidSudoku(board)
    print(b)