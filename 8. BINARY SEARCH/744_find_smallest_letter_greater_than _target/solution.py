"""
Given a list of sorted characters letters containing only lowercase letters, 
and given a target letter target, find the smallest element in the list 
that is larger than the given target.
Letters also wrap around. For example, 
if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]


    def nextGreatestLetter2(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        if n == 0:
            return None
        
        low = 0
        high = n - 1
        # If it can not be found, must be the first element (wrap around)
        result = 0 
        
        while low <= high:
            mid = low + (high-low) // 2
            if letters[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return letters[result]