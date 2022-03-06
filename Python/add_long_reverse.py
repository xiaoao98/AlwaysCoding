class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        while self:
            print(self.val)
            self = self.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)
            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c
    d = Solution().addTwoNumbers(a, c)
    ListNode.print_node(d)



