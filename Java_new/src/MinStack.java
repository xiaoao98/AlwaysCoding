import java.util.LinkedList;

public class MinStack {
    private int min;
    private LinkedList<Integer> minStack;
    public MinStack() {
        this.min = Integer.MAX_VALUE;
        this.minStack = new LinkedList<>();
    }

    public void push(int val) {
        this.minStack.add(val);
        if (val < this.min) {
            this.min = val;
        }
    }

    public void pop() {
        this.minStack.removeLast();
    }

    public int top() {
        return this.minStack.peekLast();
    }

    public int getMin() {
        return this.min;
    }

    public static void main(String[] args) {
        System.out.println(Integer.MIN_VALUE);
    }
}
