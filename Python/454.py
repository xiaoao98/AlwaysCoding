class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        dic = {}
        for c in C:
            for d in D:
                if c + d not in dic:
                    dic[c + d] = 1
                else:
                    dic[c + d] += 1

        def ksumcount(numss, target, k):
            output = 0
            if (sum([nums[0] for nums in numss]) > target) or (sum([nums[-1] for nums in numss]) < target):
                return output
            if k == 2:
                return twosumcount(target)
            tmp = 0
            for i in range(len(numss[0])):
                if i != 0 and numss[0][i] == numss[0][i - 1]:
                    output += tmp
                else:
                    tmp = ksumcount(numss[1:], target - numss[0][i], k - 1)
                    output += tmp
            return output

        def twosumcount(target):
            if target in dic:
                return dic[target]
            else:
                return 0

        return ksumcount([A, B, C, D], 0, 4)


if __name__ == '__main__':
    a = Solution()
    b = a.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
    print(b)
