if __name__ == '__main__':
    r = 2
    c = 2
    n = 3
    m1 = [[1,2,3], [1,2,3]]
    m2 = [[1,2], [2,3], [3,1]]
    output = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            for m in range(n):
                output[i][j] += m1[i][m] * m2[m][j]
    print(output)