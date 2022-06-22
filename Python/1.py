class Solution():
    def convert(self, str, numRows):
        num = numRows*2 -2
        dic = {}
        for i, v in enumerate(str):
            i = i + 1
            if i % num == 0:
                num_1 = i//num - 1
                num_2 = num
            else:
                num_1 = i // num
                num_2 = i % num
            if num_2 <= numRows:
                num_row = num_2
                num_col = num_1*(numRows-1)+1
            if num_2 > numRows:
                num_row = numRows - num_2 % numRows
                num_col = num_1*(numRows-1)+num_2%numRows+1
            dic[(num_row, num_col)] = v
        # print(dic)
        dic = sorted(dic.items(), key=lambda x:x[0][1])
        dic = sorted(dic, key=lambda x:x[0][0])
        output = ''
        for s in dic:
            output += s[1]
        print(output)


if __name__ == '__main__':
    a = Solution()
    a.convert('leetcodebest', 4)
