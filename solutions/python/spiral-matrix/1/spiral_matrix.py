def spiral_matrix(size):
    m = [[0 for x in range(size)] for y in range(size)]
    r1 = 0
    r2 = size
    c1 = 0
    c2 = size
    n = 1
    while n <= size**2:
        for c in range(c1, c2):
            m[r1][c] = n
            n += 1 
        for r in range(r1+1, r2):
            m[r][c2-1] = n
            n += 1
        for c in range(c2-2, c1-1, -1):
            m[r2-1][c] = n
            n += 1
        for r in range(r2-2, r1, -1):
            m[r][c1] = n
            n += 1
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return m 
