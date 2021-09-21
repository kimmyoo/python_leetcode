class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        m = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs', 
            8: 'tuv',
            9: 'wxyz'
        }
        
        res = ['']
        
        for digit in digits:
            temp = []
            for ch in m[int(digit)]:
                for stg in res:
                    temp.append(stg + ch)
            # print(temp)
            res = temp
        return res



    def letterCombinations2(self, digits):
        if not digits:
            return []
        m = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        ret = []
        self.dfs(m, digits, "", ret)
        return ret
    
    def dfs(self, m, digits, path, ret):
        if not digits:
            ret.append(path)
            return 
        for c in m[digits[0]]:
            self.dfs(m, digits[1:], path+c, ret)