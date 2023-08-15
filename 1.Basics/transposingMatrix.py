def transpose1 (m):
    if not m:
        return []
    
    w = len(m[0])
    h = len(m)
    result = [[None] * h for i in range(w)]
    for i in range(h):
        for j in range(w):
            result[j][i] = m[i][j]
    return result

def transpose2 (m):
    # returns an iterator of tuples
    return list(zip(*m))


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("original Matrix:", matrix)
    res1 = transpose1(matrix)
    print("method1:", res1)
    res2 = transpose2(matrix)
    print("method2:", res2)


