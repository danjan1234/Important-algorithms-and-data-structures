# With dummy nodes
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._dic = {}              # key -> node
        self._head = Node(-1, -1)   # Dummy head
        self._tail = Node(-1, -1)   # Dummy tail
        self._head.next, self._tail.prev = self._tail, self._head   # h <-> t
        self._capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self._dic.get(key)
        if node is None:
            return -1
        self._move_to_tail(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self._dic.get(key)
        if node is not None:
            node.val = value
            self._move_to_tail(node)
        else:
            node = Node(key, value)
            if len(self._dic) == self._capacity:
                self._remove_head()
            self._append_to_tail(node)
            self._dic[key] = node
    
    def _move_to_tail(self, node):
        """Disconnect the node from the doubly linked list and move it to the tail."""
        node_prev, node_next = node.prev, node.next
        node.prev, node.next = None, None
        node_prev.next, node_next.prev = node_next, node_prev
        self._append_to_tail(node)
    
    def _append_to_tail(self, node):
        """Append a free node to the tail of the doubly linked list."""
        tail_prev = self._tail.prev
        tail_prev.next = self._tail.prev = node
        node.prev, node.next = tail_prev, self._tail
   
    def _remove_head(self):
        """Remove the head node and delete it from the hashmap."""
        node, node_next = self._head.next, self._head.next.next
        self._head.next, node_next.prev = node_next, self._head
        self._dic.pop(node.key)

        