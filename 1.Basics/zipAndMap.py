if __name__ == "__main__":
    # zip(iter1, iter2, ...)
    hrs = [4, 6, 2]
    mins = [13, 9, 52]
    seconds = [33, 23, 4]
    result0 = zip(hrs, mins, seconds)
    for t in result0:
        # t is a tuple
        print(t)
    # zip object
    print(result0)
    print(list(result0))




    # map(fun, iter)
    numbers = (1, 2, 3, 4)
    numbersList = [4, 5, 6, 7]
    result = map(lambda x: x+x, numbers)
    result2 = map(lambda x: x+x, numbersList)

    # map object
    print(result)
    print(list(result))
    print(result2)
    print(list(result2))
