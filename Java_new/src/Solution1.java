import java.util.HashMap;
import java.util.HashSet;

public class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> store = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            if (store.containsKey(target-nums[i])) {
                return new int[] {store.get(target-nums[i]), i};
            }
            else {
                store.put(nums[i], i);
            }
        }
        return null;
    }
}
