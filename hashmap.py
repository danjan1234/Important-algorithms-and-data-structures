# Implement Python HashMap
# HashMap is a data structure that maps keys to values with support for insertion
# deletion, searching, and modification in O(1) time in general
# Initial values passed to the constructor: initial capacity, load factor
# Methods to support:
#   put(key, val): need to consider if key exits (modification) or not
#   get(key): get the corresponding value to the key
#   remove(key): remove entry
#   size(): number of entries
#   _rehash(): for internal usage


class Entry:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashMap:
    """
    Attributes:
        self._entries: array of Entry (ListNode) heads
    """

    def __init__(self, capacity=11, load_factor=0.75, auto_expand=True):
        """
        capacity: initial capacity
        load_factor: maximum load factor, i.e., number of entries / number of buckets
        """
        self._entries = [None for _ in range(capacity)]
        self._load_factor = load_factor
        self._size = 0
        self._auto_expand = auto_expand

    def _get_index(self, key, size=None):
        """
        Return the key's corresponding index on the entry array
        """
        if size is None:
            return self._hash(key) % len(self._entries)
        else:
            return self._hash(key) % size

    def _hash(self, key):
        """
        May deal with corners cases such as non-hashable key
        """
        return hash(key)

    def _equals(self, k1, k2):
        """
        May deal with corner cases such as equality cannot be tested between two keys
        """
        return k1 == k2

    def put(self, key, val):
        """
        Case 1: the maximum load factor has reached, rehash
        Case 2: the key does not exist, create a new entry
        Case 3: the key exists, modify the current entry
        """
        if self._size / len(self._entries) > self._load_factor and self._auto_expand:
            self._rehash()

        index = self._get_index(key)
        
        # Check if key already exits
        curr = self._entries[index]
        while curr is not None and not self._equals(curr.key, key):
            curr = curr.next

        rtn = None
        # Case 1: key does not exist
        # Case 2: otherwise
        if curr is None:
            new_entry = Entry(key, val)
            new_entry.next = self._entries[index]
            self._entries[index] = new_entry
            self._size += 1
        else:
            rtn = curr.val
            curr.val = val

        return rtn

    def get(self, key):
        """
        Case 1: key does not exist, return None
        Case 2: otherwise, return the value
        """
        index = self._get_index(key)
        curr = self._entries[index]

        while curr is not None and not self._equals(curr.key, key):
            curr = curr.next
        
        # Key is found
        if curr is not None:
            return curr.val

    def remove(self, key):
        """
        Case 1: key does not exit, do nothing
        Case 2: otherwise, remove a node in a similar manner as in linked list
        """
        index = self._get_index(key)

        # Head is None or head.key == key
        if self._entries[index] is None:
            return
        elif self._equals(self._entries[index].key, key):
            self._entries[index] = self._entries[index].next
            self._size -= 1
            return

        # Search key and perform deletion only if the next entry's key == key
        curr = self._entries[index]
        while curr.next is not None and not self._equals(curr.next.key, key):
            curr = curr.next

        rtn = None
        if curr.next is not None:
            rtn = curr.next.val
            curr.next = curr.next.next
            self._size -= 1

        return rtn

    def size(self):
        """
        Return the number of entries
        """
        return self._size

    def n_buckets(self):
        """
        Return the number of buckets
        """
        return len(self._entries)

    def is_empty(self):
        return self._size == 0

    def _rehash(self):
        new_entries = [None for _ in range(len(self._entries) * 2)]
        new_size = len(new_entries)

        for i in range(len(self._entries)):
            curr = self._entries[i]
            while curr is not None:
                next = curr.next
                new_index = self._get_index(curr.key, new_size)
                curr.next = new_entries[new_index]
                new_entries[new_index] = curr
                curr = next

        self._entries = new_entries


if __name__ == '__main__':
    # Initialization
    map = HashMap(capacity=5, load_factor=0.5)

    test = "Test hash collision"
    map._auto_expand = False
    import string
    for i, letter in enumerate(string.ascii_lowercase):
        map.put(letter, i)
    for i, letter in enumerate(string.ascii_lowercase):
        assert i == map.get(letter)
    print("{} Map size and number of entries: {}, {}".format(test, map.size(), map.n_buckets()))

    test = "Test expansion"
    map._auto_expand = True
    for i, letter in enumerate(string.ascii_uppercase):
        map.put(letter, i * 10)
    for i, letter in enumerate(string.ascii_lowercase):
        assert i == map.get(letter)
    for i, letter in enumerate(string.ascii_uppercase):
        assert i * 10 == map.get(letter)
    print("{} Map size and number of entries: {}, {}".format(test, map.size(), map.n_buckets()))

    test = "Test modification"
    for i, letter in enumerate(string.ascii_lowercase):
        map.put(letter, i * 100)
    for i, letter in enumerate(string.ascii_lowercase):
        assert i * 100 == map.get(letter)
    print("{} Map size and number of entries: {}, {}".format(test, map.size(), map.n_buckets()))

    test = "Test deletion"
    for letter in string.ascii_lowercase:
        map.remove(letter)
    for i, letter in enumerate(string.ascii_uppercase):
        assert i * 10 == map.get(letter)
    print("{} Map size and number of entries: {}, {}".format(test, map.size(), map.n_buckets()))
