import java.util.Comparator;
import java.util.PriorityQueue;

public class MergekSortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode dummy = new ListNode();
        ListNode node = dummy;
        PriorityQueue<ListNode> heap= new PriorityQueue<>((o1, o2)->(o1.val-o2.val));
        for (ListNode list: lists) {
            if (list!=null) heap.add(list);
        }
        while (!heap.isEmpty()) {
            ListNode tmp = heap.poll();
            node.next = tmp;
            node = node.next;
            if (tmp.next != null) heap.add(tmp.next);
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2);
        ListNode l2 = new ListNode(3);
        ListNode l3 = new ListNode(1);
        ListNode l4 = new ListNode(5);
        ListNode l5 = new ListNode(4);
        l1.next = l2;
        l3.next = l4;
        MergekSortedLists merge = new MergekSortedLists();
        l1 = merge.mergeKLists(new ListNode[]{l1, l3, l5});
        System.out.println(l1.next.next.val);
    }
}
