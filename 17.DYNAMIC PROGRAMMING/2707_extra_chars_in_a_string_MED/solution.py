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

    def insert(self, word: list[str]) -> None:
        current = self.root
        for letter in word:
            #if defaultdict is used, if conditional can be omitted.
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_word = True


    def isWord(self, word: list[str]) -> bool:
        current = self.root
        for letter in word:
            #check if current letter is in keys
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_word

    # def startsWith(self, prefix:str) -> bool:
    #     current = self.root
    #     for letter in prefix:
    #         if letter not in current.children:
    #             return False
    #         current = current.children[letter]
    #     return True



class Solution(object):
    def minExtraChar(self, s:str, dictionary:list[str]):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # build the trie
        t = Trie()
        for word in dictionary:
            t.insert(word)

        n = len(s)

        def dp(startIndex):
            # base case: start index reaches to end of string
            # you check this at each recurisve call
            if startIndex == n:
                return 0
            # moving forward we will count the current ch at current index
            # as a extra char
            # if it is an extra we need to add 1 to the result of next position 
            ans = dp(startIndex + 1) + 1
            # however this is not the end
            # we need to try all possible end positions 
            # by iteration over the string starting from end = start
            node = t.root
            for end in range(startIndex, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    # update the ans by comparing current ans and the point beyong this postion
                    ans = min(ans, dp(end+1))
            return ans
        return dp(0)

            

s = Solution()
str = "helloopqworld"
dictionary = ["world", "hello"]
res = s.minExtraChar(str, dictionary)
print(res)