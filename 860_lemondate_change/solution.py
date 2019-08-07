"""
At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you, 
and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  
You must provide the correct change to each customer, 
so that the net transaction is that the customer pays $5.
Note that you don't have any change in hand at first.
Return true if and only if you can provide every customer with correct change.

if first bill is larger than 5 return false

for bill in bills
    if bill is 5:
        update numof5, 
    elif  bill is 10: 
        if numof5 is == 0:
            return false
        update numof10  +=1
        update numof5   -=1
    elif bill is 20:
        if numof10 >=1 and numof5 >= 1:
            update numof10
            update numof5
        elif numof10 < 1 and numof5 >= 3
            update numof5 -=3
        else:
            return false
return true
            
"""
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        self.numDict = {'5':0, '10':0}
        
        if bills[0] >= 10:
            return False

        for bill in bills:
            if bill == 10:
                if self.numDict['5'] == 0:
                    return False
                self.numDict['5']-=1
                self.numDict['10'] +=1
            elif bill == 20:
                if self.numDict['10']>=1 and self.numDict['5'] >= 1:
                    self.numDict['10'] -= 1
                    self.numDict['5'] -= 1
                elif self.numDict['10'] == 0 and self.numDict['5'] >= 3:
                    self.numDict['5'] -= 3
                else:
                    return False
            else:
                self.numDict['5'] += 1
        return True

#test 
s = Solution()
bills_a = [5,5,10,10,20]
bills_b = [5,5,10]
res1 = s.lemonadeChange(bills_a)
res2 = s.lemonadeChange(bills_b)
print(res1, res2)


