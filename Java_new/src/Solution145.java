import java.util.LinkedList;
import java.util.List;

public class Solution145 {
    private List<Integer> postorder = new LinkedList<>();
    public List<Integer> postorderTraversal(TreeNode root) {
        postorderTraversalHelper(root);
        return postorder;
    }

    private void postorderTraversalHelper(TreeNode node) {
        if (node == null) return;
        postorderTraversalHelper(node.left);
        postorderTraversalHelper(node.right);
        this.postorder.add(node.val);
    }
}
