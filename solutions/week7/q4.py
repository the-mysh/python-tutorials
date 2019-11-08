def areTriangular(a,b,c):
    return (a <= b + c) and (b <= a + c) and (c <= a + b)
