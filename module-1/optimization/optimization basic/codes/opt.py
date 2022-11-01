import cvxpy as cp
import sympy as sp
import numpy as np
x=cp.Variable()
f =x
constraints = [2*x+5120>=4*x+2560,2*x+5120<=6*x+3840]
obj = cp.Minimize(f)
prob = cp.Problem(obj , constraints)
prob.solve()
print((f.value))
obj1 = cp.Maximize(f)
prob1 = cp.Problem(obj1 , constraints)
prob1.solve()
print((f.value))
