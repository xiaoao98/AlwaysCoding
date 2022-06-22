def maximumSumSubmatrix(matrix, size):
    rowSize = len(matrix)
    colSize = len(matrix[0])
    sumMatrix = [[0 for _ in range(colSize)] for _ in range(rowSize)]
    sumMatrix[0][0] = matrix[0][0]
    for i in range(1, rowSize):
        sumMatrix[i][0] = sumMatrix[i-1][0] + matrix[i][0]
    for i in range(1, colSize):
        sumMatrix[0][i] = sumMatrix[0][i-1] + matrix[0][i]
    for i in range(1, rowSize):
        for j in range(1, colSize):
            sumMatrix[i][j] = matrix[i][j] + sumMatrix[i-1][j] + sumMatrix[i][j-1] - sumMatrix[i-1][j-1]
    maxSum = float('-inf')
    for i in range(0, rowSize-size+1):
        for j in range(0, colSize-size+1):
            nowSum = sumMatrix[i+size-1][j+size-1]
            if i > 0:
                nowSum -= sumMatrix[i-1][j+size-1]
            if j > 0:
                nowSum -= sumMatrix[i+size-1][j-1]
            if i > 0 and j > 0:
                nowSum += sumMatrix[i-1][j-1]
            maxSum = max(nowSum, maxSum)
    return maxSum

if __name__ == '__main__':
    matrix = [
        [5, 3, -1, 5],
        [-7, 3, 7, 4],
        [12, 8, 0, 0],
        [1, -8, -8, 2]
    ]
    size = 2
    print(maximumSumSubmatrix(matrix, size))