matrix = {}
matrix[(2, 3, 4)] = 88
matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4  # ; seperates statements
if (2, 3, 6) in matrix:
    print(matrix[(2, 3, 6)])
else:
    print(0)


try:
    print(matrix[(2, 3, 6)])
except KeyError:
    print(0)

matrix.get((2, 3, 4), 0)
print(matrix)

    
