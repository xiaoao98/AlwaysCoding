import java.util.HashSet;

public class Solution141 {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy;
        ListNode fast = dummy;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                return true;
            }
        }
        return false;
//        HashSet<ListNode> store = new HashSet<>();
//        ListNode dummy = new ListNode(0);
//        dummy.next = head;
//        while (dummy.next != null) {
//            if (!store.contains(dummy.next)) {
//                store.add(dummy.next);
//            } else {
//                return true;
//            }
//            dummy = dummy.next;
//        }
//        return false;
    }
}
