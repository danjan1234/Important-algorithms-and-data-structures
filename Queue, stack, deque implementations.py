class ListNode(Object):
    def __init__(self, val):
        self.val = value
        self.next = None
        self.prev = None

# ==============================================================================
# Stack using linked list
# Three operations: push, pop, peek
# push:
#   Case 1: create a node when there is no node
#   Case 2: insert in front of the head, newNode.next = head; head = newNode
# pop:
#   Case 1: just pop, head = head.next
#   Case 2: return None if head is None

class Stack(Object):
    def __init__(self):
        self._head = None
        
    def push(self, val):
        if self._head is None:
            self._head = ListNode(val)
        else:
            newNode = ListNode(val)
            newNode.next = self._head
            self._head = newNode
    
    def pop(self, val):
        if self._head is None:
            return
        else:
            rtn = self._head.val
            self._head = self._head.next
            return rtn
    
    def peek(self, val):
        if self._head is None:
            return
        else:
            return self._head.val

# ==============================================================================
# Queue using linked list
# Operations to realize: offer, poll, peek
# offer:
#   Case 1: if empty, create a new node
#   Case 2: otherwise, add the new node to the tail
# poll:
#   Case 1: if empty, return null
#   Case 2: if not empty, remove and return the node value (be careful when there is only one node)

class Queue(Object):
    def __int__(self):
        self._head = self._tail = None
    
    def offer(self, val):
        if self._head is None:
            self._head = self._tail = ListNode(val)
        else:
            self._tail.next = ListNode(val)
            self._tail = self._tail.next
    
    def poll(self):
        if self._head is None:
            rtn = None
        elif self._head.next is None:
            rtn = self._head.val
            self._head = self._tail = None
        else:
            rtn = self._head.val
            self._head = self._head.next
        return rtn
    
    def peek(self):
        if self._head is None:
            return
        else:
            return self._head.val
            
# ==============================================================================
# Deque using linked list
# Operations: offer_first, poll_first, peek_first, offer_last, poll_last, peek_last
# offer_first:
#   Case 1: if empty, self._head = self._tail = ListNode(val)
#   Case 2: otherwise, newNode.next = self._head; self._head.prev = newNode; self._head = newNode
# poll_first:
#   Case 1: if empty, return None
#   Case 2: otherwise return the value and set self._head = self._head.next
#       Special case: if there is one node, after polling self._tail = self._head = None

class Deque:
    def __init__(self):
        self._head = self._tail = None
    
    def offer_first(self, val):
        if self._head is None:
            self._head = self._tail = ListNode(val)
        else:
            newNode = ListNode(val)
            newNode.next, self._head.prev = self._head, newNode
            self._head = newNode
    
    def poll_first(self):
        if self._head is None:
            return
        elif self._head.next is None:
            rtn = self._head.val
            self._head = self._tail = None
        else:
            rtn = self._head.val
            self._head = self._head.next
            self._head.prev = None
            retrn rtn
            
# ==============================================================================
# Stack using arraylist
class Stack:
    def __init__(self, capacity=100):
        self._arr = [None for _ in range(capacity)]
        self._pt = 0    # Points to the first available position
    
    def push(self, val):
        self._arr[_pt] = val
        self._pt += 1
        
    def pop(self):
        if self._pt == 0:
            return
        self._pt -= 1
        return self._arr[self._pt]
        
    def peek(self):
        if self._pt == 0:
            return
        return self._arr[self._pt - 1]