if __name__ == "__main__":
    d = {}
    d['a'] = 1
    d['b'] = 2
    print(d)
    print(d.get('c')) # this None
    # print(d['c']) # this is an error

    # object
    print(d.items())
    
    for k, v in d.items():
        print(k, d[k])
