class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        while self:
            print(self.val)
            self = self.next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        node = head
        tmp1 = []
        while(node!=None):
            tmp1.append(node)
            node = node.next
        tmp2 = []
        for i in range(len(tmp1)//2):
            tmp2.append(tmp1[i])
            tmp2.append(tmp1[len(tmp1)-i-1])
        if len(tmp1)%2 == 1:
            tmp2.append(tmp1[len(tmp1)//2])
        node = head
        for i in range(1, len(tmp2)):
            node.next = tmp2[i]
            node = node.next
        node.next = None


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    o = Solution().reorderList(a)
    ListNode.print_node(o)


