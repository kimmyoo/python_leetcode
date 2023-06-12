if __name__ == "__main__":
    print([None] * 3)
    print(["hello"] * 3)
    # list comprehension 
    # pay attention to the [] on the outer layer
    res = [[None] for _ in range(3)]
    print(res)