class TrieNode:
    def __init__(self) -> None:
        self.children = dict()
        self.isWord = False
    

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    

    def insertWord(self, word:str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.isWord = True


    def searchWord(self, word:str) -> bool:
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.isWord
    

    def buildTrieFromList(self, words:list[str]) -> None:
        for word in words:
            self.insertWord(word)

    def isPrefixOf(self, word:str) -> bool: 
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True


# test

words = ["the", "chemical", "brothers", "for", "that", "beautiful", "feeling"]

t = Trie()
t.buildTrieFromList(words)
print(t.root.children.keys())

searchRes = t.searchWord("chemical")
prefixSearchRes1 = t.isPrefixOf("chem")
prefixSearchRes2 = t.isPrefixOf("blue")
print(searchRes, prefixSearchRes1, prefixSearchRes2)


