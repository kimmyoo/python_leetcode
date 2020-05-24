class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        #mono stack mono increasing or decreasing
        #栈里只存放最大值 遇到比栈里大的值 就 pop() 出来 保持栈里的index 指向高的温度
        res = [0] * len(T)
        currentPeak = []
        for i in range(len(T)-1, -1, -1):
            while currentPeak and T[i] >= T[currentPeak[-1]]:
                currentPeak.pop()
            #when using a stack top element alway use if to check
            if currentPeak:
                res[i] = currentPeak[-1] - i
            currentPeak.append(i)
        return res


    def dailyTemperatures2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        #quadratic solution. exceeds time limit
        """
        res = []
        for i in range(len(T)):
            count = 0
            for j in range(i, len(T)):
                if T[j] <= T[i]: 
                    count += 1
                    if j == len(T) - 1:
                        res.append(0)
                else:
                    res.append(count)
                    break
        return res