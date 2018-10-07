"""
Implement Trie. This version's TrieNode does not contain count information. The deletion is a little bit more difficult
to implement.

Need to support the following operations:
    insert
    search
    startsWidth
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self._root
        for char in word:
            next = curr.children.get(char)
            if next is None:
                next = TrieNode()
                curr.children[char] = next
            curr = next
        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self._root
        for char in word:
            next = curr.children.get(char)
            if next is None:
                return False
            curr = next
        return curr.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self._root
        for char in prefix:
            next = curr.children.get(char)
            if next is None:
                return False
            curr = next
        return True
        
    def delete(self, word):
        """
        Delete the word if it exists. The requirement is to clear any unnecessary nodes in this trie during deletion.
        :type word: str
        :rtype: void
        """
        # Use an explicit stack to record the nodes along the path. Note the grand-root is not recorded
        stack = []
        curr = self._root
        for char in word:
            next = curr.children.get(char)
            if next is None:
                break
            curr = next
            stack.append(curr)
        
        # Word not found
        if len(stack) < len(word):
            return
        # Found word is not the leaf node
        elif len(stack[-1].children) > 0:
            stack[-1].is_word = False
        # Found word is the leaf node. Delete all unnecessary nodes
        else:
            stack[-1].is_word = False
            # Move backward along the path and find the first node which either has more than 2 splits or is a word
            while len(stack) > 0 and len(stack[-1].children) <= 1 and not stack[-1].is_word:
                node = stack.pop()
            if len(stack) > 0:
                stack[-1].children.pop(word[len(stack)])
            else:
                self._root.children.pop(word[0])
                
                
if __name__ == '__main__':
    trie = Trie()
    
    print("Insert apple")
    print(trie.insert("apple"))
    
    print("Search apple")
    print(trie.search("apple"))
    
    print("Insert app")
    print(trie.insert("app"))
    
    print("Search app")
    print(trie.search("app"))
    
    print("Delete app")
    print(trie.delete("app"))
    
    print("Search apple")
    print(trie.search("apple"))
    
    print("Search app")
    print(trie.search("app"))

    print("Delete app")
    print(trie.delete("app"))
    
    print("Search app")
    print(trie.search("app"))
    
    print("Search apple")
    print(trie.search("apple"))
    
    print("Number of grand-root's splits is: {}".format(len(trie._root.children)))
