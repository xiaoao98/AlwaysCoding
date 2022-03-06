class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        output = tmp = []
        def helper(Node, sum_Node):
            if Node == None:
                return
            sum_Node += Node.val
            tmp.append(Node.val)
            if Node.left == None and Node.right == None:
                if sum_Node == sum:
                    output.append(tmp)
                return
            helper(Node.left, sum_Node)
            tmp.pop()
            helper(Node.right, sum_Node)
            tmp.pop()
        return helper(root, 0)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# if __name__ == "__main__":
#     a = Solution()
#     leaf1 = TreeNode(7)
#     leaf2 = TreeNode(2)
#     leaf3 = TreeNode(5)
#     leaf4 = TreeNode(1)
#
#     b = a.minimumTotal(nums)
#     print(b)