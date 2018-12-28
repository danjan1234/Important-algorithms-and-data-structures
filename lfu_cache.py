# With dummy nodes
class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = self.next = None

class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._dic = {}        # key -> node
        self._ht_dic = {}     # freq -> (dummy_head, dummy_tail)
        self._cap = capacity
        self._min_freq = 1    # Minimum frequency

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self._dic.get(key)
        if node is None:
            return -1
        self._move_to_head_of_higher_freq_list(node)
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
            self._move_to_head_of_higher_freq_list(node)
        elif self._cap == 0:
            return
        else:
            node = Node(key, value, 1)
            if len(self._dic) == self._cap:
                self._remove_least_used()
            self._dic[key] = node
            self._append_to_head_of_correct_freq_list(node)
            self._min_freq = 1
     
    def _move_to_head_of_higher_freq_list(self, node):
        """Move the node from one list to the head of another list of higher frequency."""
        # Disconnect from the current list 
        head, tail = self._ht_dic.get(node.freq)
        node_prev, node_next = node.prev, node.next
        node.prev = node.next = None
        node_prev.next, node_next.prev = node_next, node_prev
        if head.next is tail:
            self._ht_dic.pop(node.freq)
            if node.freq == self._min_freq:
                self._min_freq += 1
        
        # Append the node (now free) to the head of the list of higher frequency
        node.freq += 1
        self._append_to_head_of_correct_freq_list(node)
    
    def _remove_least_used(self):
        """Remove the least frequently and least recent used node."""
        head, tail = self._ht_dic.get(self._min_freq)
        node, node_prev = tail.prev, tail.prev.prev
        node_prev.next, tail.prev = tail, node_prev
        if head.next is tail:
            self._ht_dic.pop(self._min_freq)
        self._dic.pop(node.key)
     
    def _append_to_head_of_correct_freq_list(self, node):
        """Append a free node to the head of the linked list of the correct frequency."""
        ht = self._ht_dic.get(node.freq)
        if ht is None:
            head = Node(-1, -1, node.freq)
            tail = Node(-1, -1, node.freq)
            head.next, tail.prev = tail, head
            self._ht_dic[node.freq] = (head, tail)
        else:
            head, tail = ht
        head_next = head.next
        head.next = head_next.prev = node
        node.prev, node.next = head, head_next


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
