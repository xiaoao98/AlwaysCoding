import java.util.HashSet;

public class Solution160 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
//        if (headA == null || headB == null) return null;
//        HashSet<ListNode> A = new HashSet<>();
//        while( headA != null) {
//            A.add(headA);
//            headA= headA.next;
//        }
//        while( headB != null) {
//            if (A.contains(headB)) return headB;
//            headB= headB.next;
//        }
//        return null;
        ListNode nodeA = headA;
        ListNode nodeB = headB;
        while (nodeA != nodeB) {
            nodeA = nodeA == null? headB: nodeA.next;
            nodeB = nodeB == null? headA: nodeB.next;
        }
        return nodeA;
    }
}
