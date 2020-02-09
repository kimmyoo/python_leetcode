class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        #主要是找count 里面最小数的 common divisors
        #然后在看是不是所有count都可以被divsors里面的其中一个整除
        d = {}
        for c in deck:
            if c not in d:
                d[c] = 1
            else:
                d[c] +=1
        #find the minimum of the values in dict
        minimum = min(d.values())
        if minimum == 1:
            return False
        else:
            divisors = self.allDivisors(minimum)
            for k, v in d.items():
                #感觉自己这里any()用的不错
                res = [v % div == 0 for div in divisors]
                if any(res):
                    continue
                else:
                    return False
            return True
        
    def allDivisors(self, number):
        """
        :type number: int
        :rtype: List[int]
        """
        divrs = []
        sr = math.sqrt(number)
        i = 1
        while i <= sr:
            if number % i == 0:
                if number/i == i:
                    divrs.append(i)
                else:
                    divrs.append(i)
                    divrs.append(number/i)
            i+=1
        divrs.remove(1)
        return divrs