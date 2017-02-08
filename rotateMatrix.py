'''
Cracking the Coding Interview
1.7
p.91
'''

def rotateMatrix(mat):
    n = len(mat)
    for i in range(n / 2):
        first = i
        last = n - 1 - i
        for sq in range(first, last):
            temp = mat[sq][first]
            mat[sq][first] = mat[first][last - sq]
            mat[first][last - sq] = mat[last - sq][last]
            mat[last - sq][last] = mat[last][sq]
            mat[last][sq] = temp
    return mat
            

a = [[1,2,3],[4,5,6],[7,8,9]]
print rotateMatrix(a)