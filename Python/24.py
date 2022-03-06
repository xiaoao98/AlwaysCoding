class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        while self:
            print(self.val)
            self = self.next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        node = head
        last_node = head
        head = head.next
        while(node!= None and node.next != None):
            last_node.next = node.next
            last_node = node
            # node, node.next, node.next.next = node.next.next, node.next.next, node
            node.next.next, node.next = node, node.next.next
            node = node.next
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    e = Solution().swapPairs(a)
    ListNode.print_node(e)


