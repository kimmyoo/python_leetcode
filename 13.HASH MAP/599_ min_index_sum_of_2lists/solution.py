"""
Suppose Andy and Doris want to choose a restaurant for dinner, 
and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. 
If there is a choice tie between answers, output all of them with no order requirement. 
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
"""
#my own solution
import sys
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        sumOfIndex = sys.maxsize
        d = {}
        #add ele to d
        for e in list1:
            if e not in d:
                d[e] = 1
        #update common interest and add rest of elements in list2 to d
        for e in list2:
            if e in d:
                d[e] +=1
            else:
                d[e] = 1
        
        #replace 2 with index sum. if sum is less than previous one update sum
        #and replace elements that appear only once with -1 (because index sum can never be negative)
        for k in d:
            if d[k] == 2:
                d[k] = list1.index(k) + list2.index(k) 
                if d[k] <= sumOfIndex:
                    sumOfIndex = d[k]
            else:
                d[k] = -1
        #loop through d and add elements that appeared sumOfIndex times to res
        for k in d:
            if d[k] == sumOfIndex:
                res.append(k)
        
        return res
                