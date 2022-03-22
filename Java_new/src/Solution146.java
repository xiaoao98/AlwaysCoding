import java.util.HashMap;

public class Solution146 {

}

class LRUCache {
    class doubleLinkedList {
        int key;
        int value;
        doubleLinkedList next;
        doubleLinkedList prev;
        doubleLinkedList() {
            next = null;
            prev = null;
            value = -1;
            key = -1;
        }
    }

    void moveToLast(doubleLinkedList node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        insertToLast(node);
    }

    void insertToLast(doubleLinkedList node) {
        tail.prev.next = node;
        node.prev = tail.prev;
        tail.prev = node;
        node.next = tail;
    }

    doubleLinkedList deleteFirst() {
        doubleLinkedList tmp = head.next;
        head.next = head.next.next;
        head.next.prev = head;
        return tmp;
    }

    private int capacity;
    private int num;
    private doubleLinkedList head;
    private doubleLinkedList tail;
    private HashMap<Integer, doubleLinkedList> storage= new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.num = 0;
        head = new doubleLinkedList();
        tail = new doubleLinkedList();
        head.next = tail;
        tail.prev = head;
    }



    public int get(int key) {
        if (storage.containsKey(key)) {
            moveToLast(storage.get(key));
            return storage.get(key).value;
        }
        else {
            return -1;
        }
    }

    public void put(int key, int value) {
        doubleLinkedList node = storage.get(key);
        if (node == null) {
            doubleLinkedList newNode = new doubleLinkedList();
            insertToLast(newNode);
            newNode.key = key;
            newNode.value = value;
            storage.put(key, newNode);
            num++;
            if (num > capacity) {
                doubleLinkedList first = deleteFirst();
                storage.remove(first.key);
                num--;
            }
        }
        else {
            node.value = value;
            moveToLast(node);
        }

    }
}
