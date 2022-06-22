import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    int[][] matrix;
    List<Integer> output;
    public List<Integer> spiralOrder(int[][] matrix) {
        output = new ArrayList<>();
        if (matrix.length==0) return output;
        this.matrix = matrix;
        int row = matrix.length;
        int col = matrix[0].length;
        spiralHelper(0, 0, row-1, col-1);
        return output;
    }

    public void spiralHelper(int r1, int c1, int r2, int c2) {
        if (r1 > r2 || c1 > c2) {
            return;
        }
        if (r1 == r2) {
            for (int i=c1; i<c2; i++) {
                output.add(matrix[r1][i]);
            }
            return;
        }
        if (c1 == c2) {
            for (int i=r1; i<r2; i++) {
                output.add(matrix[i][c1]);
            }
        }
        else {
            for (int i=c1; i<c2; i++) {
                output.add(matrix[r1][i]);
            }
            for (int i=r1; i<r2; i++) {
                output.add(matrix[i][c2]);
            }
            for (int i=c2; i>c1; i--) {
                output.add(matrix[r2][i]);
            }
            for (int i=r2; i>r1; i--) {
                output.add(matrix[i][c1]);
            }
            spiralHelper(r1+1, c1+1, r2-1, c2-1);
        }
    }
}
