from random import randint
import numpy as np
from functools import reduce



def solver_python(grid):
    num = np.arange(1,10)
    m,j = np.where(grid == 0)
    if ( m.size == 0 ):
        return(True,grid)
    else:
        
        
        j = j[0]
        
        m = m[0]
        
        r = grid[m,:]
        
        C = grid[:,j]
        
        S = grid[(m // 3) * 3: ( 3 + ( m // 3 ) * 3 ),( j // 3 ) * 3:( 3 + ( j // 3 )* 3 ) ].reshape(9)
        
        Value = np.setdiff1d(num , reduce(np.union1d,(r,C,S)))
        grid_temp = np.copy(grid) 
        for value in Value:
            grid_temp[m,j] = value
            A = solver_python(grid_temp)
            if (A[0]):
                return(A)
        return(False,None)
    

    
t = np.array([[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]])

t[randint(0 , 9)][randint(0 , 9)] = randint(0 , 9)
t = solver_python(t)[1]



y = int(input(" Number Delete: "))

for m in range (y):
    t[randint(0 , 9)][randint(0 , 9)] = 0
    

    
print (t)
