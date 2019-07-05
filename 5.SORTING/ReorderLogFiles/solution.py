"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  
Then, either:
Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  I
t is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.  
The letter-logs are ordered lexicographically ignoring identifier, with 
the identifier used in case of ties.  The digit-logs should be put 
in their original order.
"""

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digitLogs = []
        letterLogs = []
        for log in logs:
            log_size = len(log)
            i = 0
            while log[i] != ' ':
                i+=1
            if log[i+1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        # list.sort(key = )
        # lambda
        letterLogs.sort(key = lambda log: log.split()[0])
        letterLogs.sort(key = lambda log: log.split()[1:])#sort by suffix
        res = letterLogs + digitLogs
        return res


#test
s = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
res = s.reorderLogFiles(logs)
print (res)
