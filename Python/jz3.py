class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        head = TreeNode(0)

        def reconstructhead(node, l1, h1, l2, h2):
            if l1 <= h1 and l2 <= h2:
                node.val = pre[l1]
                loc = tin.index(node.val)
                if l2 <= loc - 1:
                    node.left = TreeNode(0)
                    reconstructhead(node.left, l1 + 1, l1 + loc - l2, l2, loc - 1)
                if loc + 1 <= h2:
                    node.right = TreeNode(0)
                    reconstructhead(node.right, l1 + loc - l2 + 1, h1, loc + 1, h2)

        reconstructhead(head, 0, len(pre) - 1, 0, len(tin) - 1)
        return head

    def printtree(self, head):
        if head != None:
            print(head.val)
            self.printtree(head.left)
            self.printtree(head.right)


if __name__ == '__main__':
    # a = Solution()
    # b = a.reConstructBinaryTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    # a.printtree(b)
    a = TreeNode(1)
    b = a.left
    b = TreeNode(3)
    print(b.val)