import java.util.ArrayList;
import java.util.Collections;
final class TreeInfo {
    public int height;
    public final boolean balanced;

    public TreeInfo(int height, boolean balanced) {
        this.height = height;
        this.balanced = balanced;
    }
}
public class Solution110 {
    public boolean isBalanced(TreeNode root) {
        if ( root == null) return true;
        int heightRoot = height(root);
        return heightRoot>0;
    }

    public int height(TreeNode node){
        if (node == null) {
            return 0;
        }
        int heightLeft = height(node.left);
        int heightRight = height(node.right);
        if (heightLeft == -1 || heightRight == -1) {return -1;}
        if (Math.abs(heightLeft-heightRight) > 1) {
            return -1;
        }
        return Math.max(heightLeft, heightRight)+1;
    }
}
