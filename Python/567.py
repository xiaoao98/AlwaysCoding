from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dic = Counter(s1)
        slide_dic = Counter(s2[:len(s1)])
        count = 0
        for i in s1_dic:
            if s1_dic[i] == slide_dic[i]:
                count += 1
        if count == len(s1_dic):
            return True

        for i in range(len(s1), len(s2)):
            ele = s2[i]
            if ele in s1_dic:
                if ele in slide_dic:
                    if slide_dic[ele] == s1_dic[ele]:
                        count -= 1
                    slide_dic[ele] += 1
                else:
                    slide_dic[ele] = 1
                if slide_dic[ele] == s1_dic[ele]:
                    count += 1
            ele = s2[i - len(s1)]
            if ele in s1_dic:
                if slide_dic[ele] == s1_dic[ele]:
                    count -= 1
                slide_dic[ele] -= 1

                if slide_dic[ele] == s1_dic[ele]:
                    count += 1
            if count == len(s1_dic):
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    output = solution.checkInclusion("abc", "ccccbbbbaaaa")
    print(output)