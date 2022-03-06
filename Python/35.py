if __name__ == "__main__":
    n = 17
    tmp = [[]]
    def helper(n):
        if n == 1:
            tmp[0].append(1)
        else:
            helper(n-1)
            for i in range(n-1):
                tmp[i].append(tmp[i][n-i-2]+n)
            tmp.append([tmp[n-2][0]+n-1])
    helper(n)
    for outputs in tmp:
        outputs = map(str, outputs)
        print(' '.join(outputs))