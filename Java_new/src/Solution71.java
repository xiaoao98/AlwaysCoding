import java.util.LinkedList;
import java.util.Stack;

public class Solution71 {
    public String simplifyPath(String path) {
        String[] pathArray = path.split("/");
        Stack<String> pathSimple = new Stack<>();
        for (int i=0; i< pathArray.length; i++) {
            if (pathArray[i].equals(".")) continue;
            if (pathArray[i].equals("..")) {
                if (!pathSimple.isEmpty()) {
                    pathSimple.pop();
                }
            }
            else if (!pathArray[i].equals("")){
                pathSimple.add(pathArray[i]);
            }
        }
        if (pathSimple.isEmpty()) {
            return "/";
        }
        StringBuilder sb = new StringBuilder();
        for(String s: pathSimple) {
            sb.append("/");
            sb.append(s);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution71 solution71 = new Solution71();
        System.out.println(solution71.simplifyPath("/home/"));
    }
}
