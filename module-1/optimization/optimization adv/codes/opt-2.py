import cvxpy  as cp
import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(0,'/sdcard/fwc/matrices/CoordGeo')

#if using termux
import subprocess
import shlex
#Defining f(x)

def f(x,a,b,c,d):
        return a * x**3 + b * x**2 + c * x + d
        
        
a = 19
b = 0
c = -57
d = 34
label_str = "$19x^3-57x+34=0$"

#For minima using gradient ascent
cur_x = 1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 3*a*x**2 + 2*b*x + c           



#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x,a,b,c,d)
print("Minimum value of f(x) is ", min_val, "at","x =",cur_x)

#For maxima using gradient ascent
cur_x1 = -1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0
  

#Gradient decent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x1 = cur_x1            
    cur_x1 -= alpha * df(prev_x1)   
    previous_step_size = abs(cur_x1 - prev_x1)   
    iters+=1  

max_val = f(cur_x1,a,b,c,d)
print("Maximum value of f(x) is ", max_val, "at","x =",cur_x1)

#Plotting f(x)
x=np.linspace(-5,5,100)
y=f(x,a,b,c,d)
plt.plot(x,y,label=label_str)


#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')
plt.plot(cur_x1,max_val,'o')
plt.text(cur_x1, max_val,f'Q({cur_x1:.4f},{max_val:.4f})')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.show()
plt.savefig('/sdcard/fwc/opt/optadv/optadv.pdf')
