import java.util.ArrayDeque;
import java.util.PriorityQueue;

public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length==0) return new int[] {0};
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int i=0; i<k; i++) {
            clear(queue, nums, i);
            queue.add(i);
        }
        int[] output = new int[nums.length-k+1];
        output[0] = nums[queue.getFirst()];
        for (int i=k; i<nums.length; i++) {
            if (queue.getFirst()==i-k) queue.removeFirst();
            clear(queue, nums, i);
            queue.add(i);
            output[i-k+1] = nums[queue.getFirst()];
        }
        return output;
    }
    private void clear(ArrayDeque<Integer> queue, int[] nums, int i) {
        while(!queue.isEmpty() && nums[queue.getLast()] < nums[i]) {
            queue.removeLast();
        }
    }
}
