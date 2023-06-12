if __name__ == "__main__":
    strs = ['abc', 'milk', 'giraffe', 'superstar dj', 'here', 'we', 'go']
    # key is a function; could be built-in function
    # or an anonymous function. like a lambda function
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
