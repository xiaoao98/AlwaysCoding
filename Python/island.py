class Island(object):
    def longest_way(self, matrix, m, n, sea_h):
        if matrix == [[]]:
            return 0

        # first step: sign out all the sea

        def sea(matrix, r, c, m, n):
            if matrix[r][c] <= sea_h:
                matrix[r][c] = 2**15
                if r-1 >= 0:
                    sea(matrix, r-1, c, m, n)
                if r+1 <= m-1:
                    sea(matrix, r+1, c, m, n)
                if c-1 >= 0:
                    sea(matrix, r, c-1, m, n)
                if c+1 <= n-1:
                    sea(matrix, r, c+1, m, n)
            return

        for i in range(n):
            sea(matrix, 0, i, m, n)
            sea(matrix, m-1, i, m, n)
        for i in range(1, m-1):
            sea(matrix, i, 0, m, n)
            sea(matrix, i, n-1, m, n)

        # second step: find the max length (use dp to lessen the time complexity)

        def helper(matrix, r, c, m, n):
            if dp[r][c] != 0:
                return dp[r][c]
            tmp1 = tmp2 = tmp3 = tmp4 = 0
            if r-1 >= 0 and matrix[r-1][c] != 2**15 and matrix[r-1][c] > matrix[r][c]:
                tmp1 = helper(matrix, r-1, c, m, n)
            if r+1 <= m-1 and matrix[r+1][c] != 2**15 and matrix[r+1][c] > matrix[r][c]:
                tmp2 = helper(matrix, r+1, c, m, n)
            if c-1 >= 0 and matrix[r][c-1] != 2**15 and matrix[r][c-1] > matrix[r][c]:
                tmp3 = helper(matrix, r, c-1, m, n)
            if c+1 <= n-1 and matrix[r][c+1] != 2**15 and matrix[r][c+1] > matrix[r][c]:
                tmp4 = helper(matrix, r, c+1, m, n)
            tmp = max(tmp1, tmp2, tmp3, tmp4) + 1
            dp[r][c] = tmp
            return tmp

        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_len = 0
        curr_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 2**15:
                    curr_len = helper(matrix, i, j, m, n)
                if max_len < curr_len:
                    max_len = curr_len
        return max_len


if __name__ == '__main__':
    sample = Island()
    island = [[14, 2, 9, 10, 11],
              [7, 0, 9, 0, 12],
              [7, 7, 10, 0, 13]]
    # sample.longest_way(island, 3, 5, 0)
    sample_output = sample.longest_way(island, 3, 5, 0)
    print(sample_output)
    # print(island)
