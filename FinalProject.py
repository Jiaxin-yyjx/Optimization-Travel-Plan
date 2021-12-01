import cvxpy as cp
import pandas as pd

n = 24
u = cp.Variable(24, integer = True)

flight = pd.read_csv('/Users/heben/Downloads/DataFind.csv') 

C = flight.values

X = cp.Variable((24, 24), boolean = True) # Vector Variables
MAX_ITER = 50
RESTARTS = 5
constraints = []
cost = 0

for i in range(n):
    for j in range(n):
        cost += (C[i,j]+35)*X[i,j]

    
for i in range(n):
   constraints.append(X[i,0] + X[i,1] + X[i,2] + X[i,3] + X[i,4] +
                      X[i,5] + X[i,6] + X[i,7] + X[i,8] + X[i,9] +
                      X[i,10] + X[i,11] + X[i,12] + X[i,13] + X[i,14] +
                      X[i,15] + X[i,16] + X[i,17] + X[i,18] + X[i,19]+ X[i,20]+ X[i,21]+ X[i,22]+ X[i,23] - X[i,i] == 1)

for j in range(n):
    constraints.append(X[0,j] + X[1,j] + X[2,j] + X[3,j] + X[4,j] +
                       X[5,j] + X[6,j] + X[7,j] + X[8,j] + X[9,j] +
                       X[10,j] + X[11,j] + X[12,j] + X[13,j] + X[14,j] +
                       X[15,j] + X[16,j] + X[17,j] + X[18,j] + X[19,j]+ X[20,j]+ X[21,j]+ X[22,j]+ X[23,j] - X[j,j] == 1)
    
for i in range(n):
    for j in range(n):
        constraints.append((C[i,j]+35)*X[i,j]<=4000)
        
        
for i in range(1, 24):
   for j in range(1, 24):
       if i == j:
          continue
       else:
           constraints.append(u[i] - u[j] + (n) * X[i, j] <= n - 1)
           
for i in range(2,24): constraints.append(u[i] >= 1)
for i in range(1,24): constraints.append(u[i] <= 23)


problem = cp.Problem(cp.Minimize(cost), constraints) 
problem.solve(solver=cp.GUROBI,verbose = True, iterations = MAX_ITER)
print("obj_func =") 
print(cost.value) 
print("X =") 
print(X.value)
X[i,i]
X[j,j]

print("u =")
print(u.value)
