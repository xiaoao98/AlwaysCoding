public class Solution59 {
    int[][] matrix;
    public void helper(int value, int start, int end) {
        if (start > end) return;
        if (start == end) {
            matrix[start][end] = value;
            return;
        }
        int value1 = value;
        int value2 = value1+end-start;
        int value3 = value2+end-start;
        int value4 = value3+end-start;
        for (int i=start; i<end; i++) {
            matrix[start][i] = value1;
            value1 ++;
            matrix[i][end] = value2;
            value2 ++;
            matrix[end][end-i+start] = value3;
            value3 ++;
            matrix[end-i+start][start] = value4;
            value4 ++;
        }
        helper(value4, start+1, end-1);

    }
    public int[][] generateMatrix(int n) {
        matrix = new int[n][n];
        helper(1, 0, n-1);
        return matrix;
    }

    public static void main(String[] args) {
        Solution59 solution59 = new Solution59();
        System.out.println(solution59.generateMatrix(4));
    }
}
