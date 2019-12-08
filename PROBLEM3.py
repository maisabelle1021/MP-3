import numpy as np   

print("Enter matrix data (row wise): ")
datapt = list(map(int,input().split()))
r = int(len(datapt)/2)
c = 2

datapt1 = len(np.array(datapt).reshape(r,c))
datapt2 = np.array(datapt).reshape(r,c)

if datapt1>=10:
    print("The polynomials are limited to until the 10th degree only. Reduce the number of data points.")
    
for i in range(datapt1):
    pxi = np.polyfit(datapt2[:,0],datapt2[:,0],i)
    pv = np.polyval(pxi,datapt2[:,0])
    pyi = np.linalg.norm(datapt2[:,1] - pv)
    vec = [i,pyi]
    
    if i ==0:
        identifier == vec
    elif identifier[1] >= vec[1] :
        deg = vec[0]
            
    pyi = np.polyfit(datapt2[:,0],datapt2[:,1],deg)
    print("coefficients",np.around(pyi,2))
        