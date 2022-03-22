class Solution21 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode mergedDummy = new ListNode(0);
        ListNode mergedNow = mergedDummy;
        while ( list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                mergedNow.next = list2;
                list2 = list2.next;
            } else {
                mergedNow.next = list1;
                list1 = list1.next;
            }
            mergedNow = mergedNow.next;
        }
        mergedNow.next = (list1==null)? list2:list1;
        return mergedDummy.next;
    }
}