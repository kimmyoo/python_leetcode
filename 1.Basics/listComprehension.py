if __name__ == "__main__":

    # str += 
    str1 = "please"
    str1 += "come in"
    print(str1)

    # use " " 把一个 iterable 连起来
    list1 = ["will", "be", "joined", "together"]
    sentence = " ".join(list1)
    print(sentence)

    str2 = "12345"
    ch1 = "+"
    print(ch1.join(str2))

    print([None] * 3)
    print(["hello"] * 3)
    # list comprehension 
    # pay attention to the [] on the outer layer
    res = [[None] for _ in range(3)]
    print(res)