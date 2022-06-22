import java.util.HashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;

public class KClosestPointstoOrigin {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]>  heap = new PriorityQueue<>((o1, o2) -> (o1[0]*o1[0]+o1[1]*o1[1])-(o2[0]*o2[0]+o2[1]*o2[1]));
        for (int i=0; i< points.length;i++) {
            heap.add(points[i]);
        }
        int[][] ret = new int[k][];
        while (k>0) {
            ret[k-1] = heap.poll();
            k--;
        }
        return ret;
    }
}
