public class MedianofTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if ((nums1 == null || nums1.length == 0) && (nums2 == null || nums2.length == 0)) {
            return 0;
        }
        if(nums1 == null || nums1.length == 0) {
            return nums2.length%2==1? nums2[nums2.length/2+1]: ((double)(nums2[nums2.length/2] + nums2[nums2.length/2+1])/2);
        }
        if(nums2 == null || nums2.length == 0) {
            return nums1.length%2==1? nums1[nums1.length/2+1]: ((double)(nums1[nums1.length/2] + nums1[nums1.length/2+1])/2);
        }
        if (nums1.length>nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int low = 0, high = nums1.length;
        int size = nums1.length + nums2.length;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (nums1[mid] < nums2[size/2-mid-1]) {
                low = mid+1;
            }
            else {
                high = mid;
            }
        }
        int first = low;
        int second = size / 2 - low;

        int shorterLeft = first == 0 ? Integer.MIN_VALUE : nums1[first - 1];
        int shorterRight = first == nums1.length ? Integer.MAX_VALUE : nums1[first];

        int longerLeft = second == 0 ? Integer.MIN_VALUE : nums2[second - 1];
        int longerRight = second == nums2.length ? Integer.MAX_VALUE : nums2[second];

        if((size % 2 == 1)) {
            return Math.min(shorterRight, longerRight);
        }else{
            return Math.max(shorterLeft, longerLeft) * 0.5 + Math.min(shorterRight, longerRight) * 0.5;
        }
    }

    public static void main(String[] args) {
        MedianofTwoSortedArrays test = new MedianofTwoSortedArrays();
        System.out.println(test.findMedianSortedArrays(new int[] {1, 3}, new int[] {2}));

    }
}
