from helper import plot
import random
# plot([[1,2],[3,4]])
# plot([[10,2],[3,4]])

def giacquan(n=1):
    k = 0
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if (i,j) != (0,0):
                # print(i,j)
                print(k)
                k+=1


giacquan(1)
print(29+24)