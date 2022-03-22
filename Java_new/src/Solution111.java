import java.util.LinkedList;

public class Solution111 {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        LinkedList<TreeNode> nodeArray = new LinkedList<>();
        nodeArray.add(root);
        int height = 1;
        while (!nodeArray.isEmpty()) {
            int size = nodeArray.size();
            for (int i=0; i<size; i++) {
                TreeNode node = nodeArray.removeFirst();
                if (node.left == null && node.right == null) {
                    return height;
                }
                if (node.left != null) {
                    nodeArray.add(node.left);
                }
                if (node.right != null) {
                    nodeArray.add(node.right);
                }
            }
            height++;
        }
        return height;
    }

    public static void main(String[] args) {
        TreeNode a = new TreeNode(3);
        TreeNode b = new TreeNode(9);
        TreeNode c = new TreeNode(20);
        TreeNode d = new TreeNode(15);
        TreeNode e = new TreeNode(7);
        a.left = b;
        a.right = c;
        c.left = d;
        c.right = e;
        Solution111 solution111 = new Solution111();
        System.out.println(solution111.minDepth(a));
    }
}
