class TreeNodeAnces {
    boolean p1;
    boolean p2;
    TreeNode treeNode;
    TreeNodeAnces(boolean p1, boolean p2, TreeNode treeNode) {
        this.p1 = p1;
        this.p2 = p2;
        this.treeNode = treeNode;
    }
}

public class LowestCommonAncestorofaBinaryTree {
    private TreeNodeAnces dfs(TreeNode node, TreeNode p, TreeNode q) {
        if (node==null) return new TreeNodeAnces(false, false, null);
        boolean p1=false;
        boolean p2=false;
        TreeNodeAnces left = dfs(node.left, p, q);
        if (left.treeNode!=null) return left;
        TreeNodeAnces right = dfs(node.right, p, q);
        if (right.treeNode!=null) return right;
        if (node==p||left.p1||right.p1) {
            p1 = true;
        }
        if (node==q||left.p2||right.p2) {
            p2 = true;
        }
        if (p1 && p2) {
            return new TreeNodeAnces(p1, p2, node);
        }
        return new TreeNodeAnces(p1, p2, null);
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return dfs(root, p, q).treeNode;
    }
}
