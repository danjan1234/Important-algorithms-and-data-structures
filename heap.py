# Implement Priority Queue in Python
# A priority queue is a heap which stores the data in a way that the global
# minimum or maximum resides at the heap top and can be found in O(1) time.
# The current global minimum or maximum can be removed from the heap and the
# new global minimum and maximum will be adjusted to the heap top in O(logn) time
# Initial variables: capacity
# Attributes: self._array
# Supported operations:
#   peek()
#   offer()
#   poll()
#   size()
#   is_empty()
# Methods for internal use:
#   sift_up()
#   sift_down()


class PriorityQueue:
    def __init__(self, capacity):
        self._array = [None for _ in range(capacity)]
        self._size = 0

    def peek(self):
        if self._size == 0:
            return
        return self._array[0]

    def offer(self, val):
        if self._size == len(self._array):
            self._expand()

        self._array[self._size] = val
        self._sift_up(self._size)
        self._size += 1

    def _expand(self):
        array = [None for _ in range(len(self._array) * 2)]
        for i, x in enumerate(self._array):
            array[i] = x
        self._array = array

    def poll(self):
        if self._size == 0:
            return
        rtn = self._array[0]
        self._size -= 1
        self._array[0] = self._array[self._size]
        self._sift_down(0)
        return rtn

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def heapify(self, array):
        self._array = array
        self._size = len(array)
        start_index = (len(array) - 2) // 2
        for i in range(start_index, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i):
        while (i - 1) // 2 >= 0 and self._array[i] < self._array[(i - 1) // 2]:
            parent_i = (i - 1) // 2
            self._array[i], self._array[parent_i] = self._array[parent_i], self._array[i]
            i = parent_i

    def _sift_down(self, i):
        while 2 * i + 1 < self._size:
            candidate_i = 2 * i + 1
            if 2 * i + 2 < self._size and self._array[2 * i + 2] < self._array[candidate_i]:
                candidate_i = 2 * i + 2
            if self._array[candidate_i] < self._array[i]:
                self._array[candidate_i], self._array[i] = self._array[i], self._array[candidate_i]
                i = candidate_i
            else:
                break


if __name__ == '__main__':
    pq = PriorityQueue(capacity=5)

    for i in range(5):
        pq.offer(i)

    print('Step 1: the current heap top is: ', pq.peek())

    for i in range(5):
        print('Step 2: remove 0 ~ 4: ', pq.poll())

    for x in [2, 3, 6, 1, 1, 2, 3, 0, 9, 5, 6, 7]:
        pq.offer(x)

    print('Step 3: the current heap top is: ', pq.peek())

    while not pq.is_empty():
        print('Step 4: remove the newly added elements: ', pq.poll())

    array = [2, 3, 1, 5, 7, 1, 3, 0, -1, 9, -5]
    pq.heapify(array)
    print('Step 5: the current heap top is: ', pq.peek())
    while not pq.is_empty():
        print('Step 6: remove the newly added elements: ', pq.poll())
