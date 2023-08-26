
def matrixChain(p, i, j):
 
    if i==j:
            return 0
            
    _min = 999
    
    for k in range(i,j):
        cost = matrixChain(p, i, k) + matrixChain(p, k+1, j) + p[i-1]*p[k]*p[j]
        if cost<_min:
            _min = cost
    return _min
    
arr = [1, 2, 3, 4, 3];
n = len(arr);
print("Minimum number of multiplications is ",
matrixChain(arr, 1, n-1));
