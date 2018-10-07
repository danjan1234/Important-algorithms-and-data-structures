// Data structures to synchronize: HashMap, doubly LinkedList's head and tail
class ListNode<K, V> {
  K key;
  V value;
  ListNode<K, V> prev, next;
  
  public ListNode(K key, V value) {
    this.key = key;
    this.value = value;
    prev = next = null;
  }
}

public class LRUCache<K, V> {
  ListNode<K, V> head, tail;
  Map<K, ListNode> map;
  int limit;
  
  // limit is the max capacity of the cache
  public LRUCache(int limit) {
    head = tail = null;
    map = new HashMap<>();
    this.limit = limit;    
  }
  
  // If key exists, reset it to the new value and move the node to the tail
  // Otherwise, create a new node and append to tail. If the limit is exceeded, delete the head
  public void set(K key, V value) {
    ListNode<K, V> curr = map.get(key);
    if (curr != null) {
      curr.value = value;
      moveExistingToTail(curr);
    } else {
      curr = new ListNode<>(key, value);
      if (tail == null) {
        head = tail = curr;
      } else {
        tail.next = curr;
        curr.prev = tail;
        tail = curr;
      }
      map.put(key, curr);
      if (map.size() > limit) {
        map.remove(head.key);
        head.next.prev = null;
        head = head.next;
        if (head == null) {
          tail = null;
        }
      } 
    }
  }
  
  public V get(K key) {
    ListNode<K, V> curr = map.get(key);
    if (curr == null) {
      return null;
    } else {
      V res = curr.value;
      moveExistingToTail(curr);
      return res;
    }
  }
  
  private void moveExistingToTail(ListNode<K, V> curr) {
    if (curr == null || curr.next == null) {
      return;
    }
    ListNode<K, V> prev, next;
    prev = curr.prev;
    next = curr.next;
    if (prev != null) {
      prev.next = next;
    } else {
      head = next;
    }
    next.prev = prev;
    tail.next = curr;
    curr.next = null;
    curr.prev = tail;
    tail = tail.next;  
  }
}
