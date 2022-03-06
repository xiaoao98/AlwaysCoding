from collections import Counter
from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        output = [[]] * (n+1)
        output[0] = [None]
        for i in range(1, n+1):
            for j in range(1, i+1):
                root = TreeNode(j)
                for lefttree in output[j-1]:
                    for righttree in output[i-j]:
                        lefttree1 = deepcopy(lefttree)
                        root.left = lefttree1
                        righttree1 = deepcopy(righttree)
                        self.treePlus(righttree1, j)
                        root.right = righttree1
                        output[i].append(root)
        return output[n]

    def treePlus(self, TreeNode, n):
        if TreeNode is not None:
            TreeNode.val += n
            if TreeNode.left is not None:
                self.treePlus(TreeNode.left, n)
            if TreeNode.right is not None:
                self.treePlus(TreeNode.right, n)


if __name__ == "__main__":
    solution = Solution()
    output = solution.generateTrees(3)
    print(output)