class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_word = True

    def findPrefix(self, word):
        """
        :type word: str
        :rtype: str
        
        if word starts with a prefix store in trie
        the prefix of the word will be returned
        otherwise, the word itself will be returned
        """
        current = self.root
        out = ''
        for letter in word:
            if letter not in current.children:
                break
            current = current.children[letter]
            out += letter
            if current.is_word:
                return out
        return word

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for root in dict:
            trie.insert(root)
        res = ""
        for word in sentence.split():
            if len(res) > 0:
                res+=" "
            res += trie.findPrefix(word)
        return res

s = Solution()
dict = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
res = s.replaceWords(dict, sentence)
print(res)