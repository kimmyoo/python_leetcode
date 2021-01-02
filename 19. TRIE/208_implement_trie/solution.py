import collections

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        #it's dictionary key is the current node's char
        #val is the child TrieNode 
        #one node can have 26 key:val pair at most

        #here we can use defaultdict(TrieNode) later we don't need to create TrieNode
        self.children = dict()
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            #if defaultdict is used, if conditional can be omitted.
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            #check if current letter is in keys
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


obj = Trie()
obj.insert("apple")
obj.insert("app")
obj.insert("apt")
param_2 = obj.search("apple")
param_3 = obj.startsWith("ap")
param_4 = obj.search("boy")
print(param_2, param_3, param_4)