class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        n = 0
        def convert(digit, n):
            d = {}
            if n == 0:
                d[10] = "X"
                d[5] = "V"
                d[1] = "I"
            elif n == 1:
                d[10] = "C"
                d[5] = "L"
                d[1] = "X"
            elif n == 2:
                d[10] = "M"
                d[5] = "D"
                d[1] = "C"
            else:
                d[1] = "M"

            if digit == 0:
                return ""
            elif 1 <= digit < 4:
                return d[1] * digit
            elif 5 <= digit < 9:
                return d[5] + d[1] * (digit - 5)
            elif digit == 4:
                return d[1] + d[5]
            else:
                return d[1] + d[10]

        while num > 0:
            digit = num % 10
            res = convert(digit, n) + res
            num /= 10
            if num < 1:
                num = 0
            n += 1
        return res


if __name__ == "__main__":
    a = Solution()
    num = 3
    b = a.intToRoman(num)
    print(b)