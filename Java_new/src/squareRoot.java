public class squareRoot {
    public static int getSquareRoot(int m) {
        int low = 1;
        int high = m;
        while (low <= high) {
            int mid = low + (high-low) / 2;
            if (m / mid > mid) low = mid + 1;
            else if (m / mid < mid) high = mid - 1;
            else return mid;
        }
        return high;
    }

    public static void main(String[] args) {
        System.out.println(getSquareRoot(145));
    }
}
