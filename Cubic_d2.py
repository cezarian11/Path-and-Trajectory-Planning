import numpy as np
import matplotlib.pyplot as plt

def mm_to_rad(T):
    return(T/180)*np.pi

di = float(500)
di =  mm_to_rad(di)
df = float(550)
df =  mm_to_rad(df)

ti = float(0) 
tf = float(50) 
x = np.arange(ti, tf, 0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 -(2*(b-a)/c**3)*t**3 #Case 1
y = cubic(x,di,df,tf)

plt.figure()
plt.title('Path Planning of d2')
plt.xlabel("time(s)") 
plt.ylabel("d2(meter)") 
plt.plot(x,y,'g',linestyle = '-')
plt.text(10,9.0, 'q(t) = a + (3t^2(b-a)/c^2)t^2 - (2t^3(b-a)/c^3)t^3')
plt.grid(True)
plt.show()