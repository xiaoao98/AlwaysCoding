import java.util.LinkedList;
import java.util.List;

public class Solution144 {
    private List<Integer> preorder = new LinkedList<>();
    public List<Integer> preorderTraversal(TreeNode root) {
        preorderTraversalHelper(root);
        return preorder;
    }

    private void preorderTraversalHelper(TreeNode node) {
        if (node == null) return;
        this.preorder.add(node.val);
        preorderTraversalHelper(node.left);
        preorderTraversalHelper(node.right);
    }
}
