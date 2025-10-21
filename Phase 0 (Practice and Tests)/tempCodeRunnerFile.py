def util(n):
    triangle = []
    for i in range(0,n):
        row = [1] * (i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j] + triangle[i-1][j-1]
        triangle.append(row)
    return triangle

print(util(5))