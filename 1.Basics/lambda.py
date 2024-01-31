if __name__ == "__main__":
    strs = ['abc', 'milk', 'giraffe', 'superstar dj', 'here', 'we', 'go']
    # key is a function; could be built-in function
    # or an anonymous function. like a lambda function
    # key specifies a function of one argument 
    # that is used to extract a comparison key from each element in iterable
    res1 = sorted(strs, key=len)
    res2 = sorted(strs, key=lambda x: x[-1])
    print(res1, '\n',  res2)

    # value after : will be returned
    # printItself is the reference to the lambda function
    # see the following example
    printItself = lambda x: x
    anotherPrintItself = printItself
    print(printItself(5))
    print(anotherPrintItself('hello lambda'))

    getSquare = lambda x: x*x
    print(getSquare(5))

    # 按照绝对值 降序 同时 负数在正数前面.
    nums = [44, -45, 2, -1, -2, 45, -44, 9, 19, -9, -19]
    def customKey(x):
        absVal = -abs(x)
        sign = -1 if x < 0 else 1
        # first compare absVal( descending), then sign 
        return (absVal, sign)
    sortedNums = sorted(nums, key=customKey)
    print(sortedNums)