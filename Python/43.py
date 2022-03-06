if __name__ == '__main__':
    r = [(0,0)]
    output = []
    mg = [['0', '1', '1'], ['0', '0', '0'], ['1', '1', '0']]
    n = 3
    m = 3
    def helper(x, y):
        if x == n-1 and y == m-1:
            for rr in r:
                output.append(rr)
            return
        if x+1 < n and mg[x+1][y] == '0':
            r.append((x+1, y))
            helper(x+1, y)
            r.pop()
        if y+1 < m and mg[x][y+1] == '0':
            r.append((x, y+1))
            helper(x, y+1)
            r.pop()
    helper(0,0)
    for o in output:
        print(o)