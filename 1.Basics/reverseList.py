def reverseList (l):
    l.reverse()
    return l

def reverseList2(l):
    res = l[ : : -1]
    return res


if __name__ == "__main__":
    myList1 = [4, 6, 2, 11, 0, -3]
    myList2 = [4, 6, 2, 11, 0, -3]
    print("original myList1:", myList1)
    print("original myList2:", myList2)

    myList1.reverse()
    res = myList2[: : -1]

    print("myList1(using .reverse()):", myList1 )
    print("myList2(using slicing):", myList2 )

