"""
For remove, using a dummy head makes it much more convenient.
"""
class Entry:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    _INITIAL_CAPACITY = 11
    _LOAD_FACTOR = 0.75

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._buckets = [None for _ in range(self._INITIAL_CAPACITY)]
        self._size = 0
        
    def size(self):
        return self._size
        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = self._get_index(key)
        curr = self._buckets[index]
        while curr is not None and not self._eq(curr.key, key):
            curr = curr.next
        if curr is None:
            entry = Entry(key, value)
            entry.next = self._buckets[index]
            self._buckets[index] = entry
            self._size += 1
            if self._size / len(self._buckets) >= self._LOAD_FACTOR:
                self._rehash()
        else:
            curr.val = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self._get_index(key)
        curr = self._buckets[index]
        while curr is not None and not self._eq(curr.key, key):
            curr = curr.next
        if curr is None:
            return -1
        else:
            return curr.val

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = self._get_index(key)
        dummy = Entry(-1, -1)
        dummy.next = self._buckets[index]
        prev, curr = dummy, dummy.next
        while curr is not None and not self._eq(curr.key, key):
            prev, curr = curr, curr.next
        if curr is None:
            return
        else:
            prev.next = prev.next.next
            self._size -= 1
            self._buckets[index] = dummy.next
    
    def _get_index(self, key, buck_array_size=None):
        if buck_array_size is None:
            buck_array_size = len(self._buckets)
        return hash(key) % buck_array_size
    
    def _eq(self, k1, k2):
        return k1 == k2
    
    def _rehash(self):
        new_buckets = [None for _ in range(len(self._buckets) * 2)]
        for head in self._buckets:
            while head is not None:
                node = head
                head = head.next
                node.next = None
                new_index = self._get_index(node.key, len(new_buckets))
                node.next = new_buckets[new_index]
                new_buckets[new_index] = node
        self._buckets = new_buckets

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)