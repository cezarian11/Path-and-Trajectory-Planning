import numpy as np
import matplotlib.pyplot as plt

def deg_to_rad(T):
    return(T/180)*np.pi

qi = float(0)
qi = deg_to_rad(qi)
qf = float(45)
qf = deg_to_rad(qf)

ti = float(0) 
tf = float(50) 
x = np.arange(ti, tf, 0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 -(2*(b-a)/c**3)*t**3 #Case 1
y = cubic(x,qi,qf,tf)

plt.figure()
plt.title('Path Planning of Theta 1')
plt.xlabel("time(s)") 
plt.ylabel("T1(radian)") 
plt.plot(x,y,'b',linestyle = '-')
plt.text(0.05, 0.7, 'q(t) = a + (3t^2(b-a)/c^2)t^2 - (2t^3(b-a)/c^3)t^3')
plt.grid(True)
plt.show()