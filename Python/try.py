import numpy as np
import pandas as pd
import bisect
import random
import math
import queue
from collections import Counter


class Solution33(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(nums, target):
            low = 0
            high = len(nums)-1
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if low == high:
                return -1
            if nums[low] <= target and nums[mid] > nums[high]:
                tmp = bisect.bisect_left(nums, target, low, mid)
                return tmp if nums[tmp] == target else -1
            elif nums[low] <= target and nums[mid] < nums[high]:
                return helper(nums[:mid], target)
            elif nums[low] >= target and nums[mid] > nums[high]:
                return helper(nums[mid+1:], target) + mid + 1
            elif nums[low] > target and nums[mid] < nums[high]:
                tmp = bisect.bisect_left(nums, target, mid+1, high)
                return tmp if nums[tmp] == target else -1

        return helper(nums, target)


class Solution1011(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        size = len(weights)
        for i in range(1, size):
            weights[i] = weights[i] + weights[i-1]
        cap = math.ceil(weights[size - 1]/D)
        while(True):
            tmp = cap
            times = 0
            while(times<D):
                loc = bisect.bisect_right(weights, tmp)
                if loc > size - 1:
                    return cap
                tmp = cap + weights[loc - 1]
                times += 1
            cap += 1


class Solution(object):
    try_it = 369

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        # self.rects = rects
        self.length = []
        self.width = []
        for rect in rects:
            self.length.append((rect[0], rect[2]))
            self.width.append((rect[1], rect[3]))
            print(Solution.try_it)

    def pick(self):
        """
        :rtype: List[int]
        """
        size = len(self.length)
        random1 = random.randint(1, size)
        length = self.length[random1 - 1]
        width = self.width[random1 - 1]
        r_l = random.randint(length[0], length[1])
        w_l = random.randint(width[0], width[1])
        print(Solution.try_it)
        return [r_l, w_l]


if __name__ == "__main__":
    df1 = pd.DataFrame({'value': [3, 29, 31]}).to_numpy()
    df2 = pd.DataFrame({'value': [1, 26, 30]}).to_numpy()
    print(type(df1))
    print(df1-df2)
    print(np.mean(df1-df2))

    # a = pd.Series([2, 3, 4])
    # b = pd.Series([1, 2, 3])
    # print(np.mean(a-b))

    # a = [[2, 4, 5], [1, 3, 6]]
    # print(a[0:1])

    # n = 4
    # solution = ["".join(['.' for _ in range(n)]) for _ in range(n)]
    # print(solution)
    #
    # size = 3
    # for i in range(size, -1, -1):
    #     print(i)
    # a = [1, 2, 3]
    # a.insert(0, 4)
    # print(a)
    # str = "ate"
    # strlist = list(str)
    # strlist2 = [v for v in str]
    # print(strlist, strlist2)

    # strlist.sort()
    # print(strlist)
    # nums = [0, 0, 0]
    # print(nums[3: 1])

    # a = Solution33()
    # b = a.search([4, 5, 6, 7, 0, 1, 2], 3)
    # print(b)
    # print(bisect.bisect_left([2, 3, 7, 10, 12], 4, 0, 1))

    # dp = [[0 for _ in range(3)] for _ in range(5)]
    # print(dp)

    # q = queue.Queue()
    # q.put(0)
    # q.put(1)
    # q.put(2)
    #
    # print(q.get())
    # print(q.get())
    # print(q.get())

    # dic = {2: [1], (3, 2): [2], 4: [3, 2]}
    # if 4 in dic:
    #     print(dic[4][1])

    # a = 1
    # def b():
    #     for i in dic:
    #         print(i)
    #     global a
    #     if (a == 1):
    #         print(a)
    #         a = 3
    #     print(a)
    # dic = {1, 3, 5}
    # b()
    # print(a)

    # a = [1, 3, 4]
    # print(sum(a))

    # s = "12345"
    # lists = list(s)
    # print(lists)
    # output = [1, 3, 4, 2, 4]
    # print("".join([str(i) for i in output]))
    # print(",".join(str(i) for i in output))
    # output = "13424"
    # print(" ".join(output))

    # a = "a    b "
    # a = a.split()
    # print(a)

    # a = [[1, 3, 4], [1, 3, 3], [4, 3, 1], [3, 1, 4]]
    # b = set()
    # for aa in a:
    #     b.add(tuple(sorted(aa)))
    # b = list(b)
    # b = list(map(list, b))
    # print(b)

    # c = 'dog'
    # char_key = 'char_{}'.format(c)
    # print(char_key)

    # nums = [1, 3, 6, 7, 9, 4, 4, 5, 6]
    # tmp = nums[0]
    # nums = nums[1:]
    # nums.append(tmp)
    # s = "sdfeafefg"
    # a = list(s)
    # print(a[-3])
    # a[0:5] = a[0:5][::-1]
    # s = "1234"
    # print(s[1:2])
    # a = [] or [2]
    # print(a)
    # l = list(s)
    # l.append("6")
    # l2 = l[:-2]
    # l2.append(l[-1]+"7")
    # print(l2)
    # print(l2[:-5])
    # print(bin(x).count('1'))
    # s = ["1234"]
    # p = ["123"]
    # p.append(s)
    # print(p)
    # a = [1, 2, 3]
    # a = a[:1] + a[1:][::-1]
    # nums = [2, 3, 1]
    # nums = nums[:1] + nums[1:][::-1]

    # a = 4
    # def test():
    #     global a
    #     a = a + 2
    #     print(a)
    # test()
    # print(a)

    # a = [[2, 2, 1], [2, 1, 2]]
    # b = [2, 2, 1]
    # if b not in a:
    #     print(1)
    # else:
    #     print(0)

    # a = [2, 13, 9, 29, 4, 47, 49]
    # c = {}
    # for i, value in enumerate(a):
    #     c[i] = value
    # d = sorted(c.items(), key=lambda lam: lam[1])
    # print(d)
    # c = sorted([(value, i) for i, value in enumerate(a)])
    # d = bisect.bisect_left(c, (24, -1))
    # print(c)
    # print(d)
    # b = bisect.bisect_left(a, 49)
    # print(b)

    # a = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
    # print(a.pick())
    #
    # print(divmod(7, 3))

    # a = b = 0
    # b += 1
    # print(a)

    # a = [3, -4, 6, -4]
    # a = map(lambda x: abs(x), a)
    # print(sum(a))

    # a = Solution1011()
    # print(a.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))

    # a = [9, 4, 2, 2, 5]
    # a = a[::-1]
    # print(a)
    # b = sorted(a)
    # bisect.insort(a, 2)
    # bisect.insort(b, 2)
    # print(a)
    # print(b)

    # a = [9, 4, 2, 2, 5]
    # b = a.pop()
    # print(b)

    # str1 = "dog cat cat dog"
    # list1 = list(str1)
    # list2 = str1.split(' ')
    # print(list1, list2)
    # for i, char in enumerate(str1):
    #     print(i, char)

    pass
