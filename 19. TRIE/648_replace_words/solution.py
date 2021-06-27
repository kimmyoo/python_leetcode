class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # build the trie with roots
    def insert(self, rt):
        cur = self.root
        for ch in rt:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        # mark the end of word or root
        cur.isWord = True
    
    # try to find the shortest root matching current word
    def findPrefix(self, original):
        output = ''
        cur = self.root
        for ch in original:
            if ch not in cur.children:
                break
            cur = cur.children[ch]
            output += ch
            # this is to ensure it will return the first met root(shortest)
            if cur.isWord:
                return output
        return original
        

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        res = ''
        t = Trie()
        for root in dict:
            t.insert(root)
        for word in sentence.split():
            if len(res) > 0:
                res += ' '
            res += t.findPrefix(word)
        # for k in t.root.children:
        #     print(k, t.root.children[k].children.items())
        return res

s = Solution()
dict = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
res = s.replaceWords(dict, sentence)
print(res)