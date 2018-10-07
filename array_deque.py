# Implement array deque using circular array in Python
# Attribute: self._array
# x x x x x x x x x
#     t     h
# Data are stored in [t, h), i.e., h is available for new element
# Initially, t = h = 0
# Conditions when empty: t == h, size == 0
# Conditions when full: t == h, size == len(self._array)
# Supported operations:
#   offer_head()
#   offer_tail()
#   peek_head()
#   peek_tail()
#   poll_head()
#   poll_tail()
#   size()
#   is_empty()
#   _expand()


class ArrayDeque:
    def __init__(self, capacity=5):
        self._array = [None for _ in range(capacity)]
        self._size = 0
        self._h = self._t = 0
        
    def _get_index(self, index):
        return index % len(self._array)

    def offer_head(self, val):
        if self._size == len(self._array):
            self._expand()
        self._array[self._h] = val
        self._h += 1
        self._h = self._get_index(self._h)
        self._size += 1

    def offer_tail(self, val):
        if self._size == len(self._array):
            self._expand()
        self._t -= 1
        self._t = self._get_index(self._t)
        self._array[self._t] = val
        self._size += 1

    def peek_head(self):
        if self._size == 0:
            return

        head_index = self._get_index(self._h - 1)
        return self._array[head_index]

    def peek_tail(self):
        if self._size == 0:
            return
        return self._array[self._t]

    def poll_head(self):
        if self._size == 0:
            return
        self._h -= 1
        self._h = self._get_index(self._h)
        self._size -= 1
        return self._array[self._h]

    def poll_tail(self):
        if self._size == 0:
            return
        rtn = self._array[self._t]
        self._t += 1
        self._t = self._get_index(self._t)
        self._size -= 1
        return rtn

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _expand(self):
        array = [None for _ in range(2 * len(self._array))]
        i = 0
        while not self.is_empty():
            array[i] = self.poll_tail()
            i += 1
        self._array = array
        self._h = self._size = i
        self._t = 0


if __name__ == '__main__':
    deque = ArrayDeque(capacity=4)
    data_range = 14

    test = "offer_head + poll_head"
    print(test)
    for i in range(data_range):
        deque.offer_head(i)
    for i in range(data_range):
        print(deque.poll_head())

    test = "offer_tail + poll_tail"
    print(test)
    for i in range(data_range):
        deque.offer_tail(i)
    for i in range(data_range):
        print(deque.poll_tail())

    test = "offer_head + poll_tail"
    print(test)
    for i in range(data_range):
        deque.offer_head(i)
    for i in range(data_range):
        print(deque.poll_tail())

    test = "offer_tail + poll_head"
    print(test)
    for i in range(data_range):
        deque.offer_tail(i)
    for i in range(data_range):
        print(deque.poll_head())
