import java.util.HashMap;

public class SubarraySumEqualsK {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> dic = new HashMap<>();
        int output = 0, sum = 0;
        dic.put(0, 1);
        for (int i=0; i<nums.length; i++) {
            sum += nums[i];
            if (dic.containsKey(sum-k)) {
                output += dic.get(sum-k);
            }
            dic.put(sum, dic.getOrDefault(sum, 0)+1);
        }
        return output;
    }
}
