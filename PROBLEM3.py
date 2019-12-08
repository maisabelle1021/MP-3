import numpy as np

print("Input values of a nx2 matrix (left to right, separated by spaces):")
matrix = list(map(int,input().split()))
r = int(len(matrix)/2)
c = 2

f1 = len(np.array(matrix).reshape(r,c))
f2 = np.array(matrix).reshape(r,c)

def PROBLEM3(f1):
    if f1 >=10:
        print("The matrix is limited up to the 10th degree only. Reduce the number of values.")
        
    for i in range(f1):
        pxi = f2[:,0]
        pyi = f2[:,1]
        pf = np.polyfit(pxi,pyi,i)
        pv = np.polyval(pf,pxi)
        a = pyi - pv
        pf = np.linalg.norm(a)
        c = [i,pf]
        
        if i == 0:
            y = c
            
        elif y[1]>=c[1]:
            new = c[0]
            
    pf = np.polyfit(pxi,pyi,new)
    print("coefficients: ", np.around(pf,2))

PROBLEM3(f1)