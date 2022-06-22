import java.util.Comparator;
import java.util.PriorityQueue;

public class KthLargestElementinanArray {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>((n1, n2)->(n2-n1));
        for (int num: nums) {
            heap.add(num);
        }
        for ( int i=0; i<k-1; i++) {
            heap.poll();
        }
        return heap.peek();
    }
}
