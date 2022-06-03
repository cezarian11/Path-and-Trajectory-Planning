import numpy as np
import matplotlib.pyplot as plt

def mm_to_meter(a):
    m = 1000
    return a/m

di = float(500)
di = mm_to_meter(di)
df = float(550)
df = mm_to_meter(df)
aci = float(45)
aci = mm_to_meter(aci)
acf = float(0.02)
acf = mm_to_meter(acf)
vi = float(0)
vi = mm_to_meter(vi)
vf = float(1)
vf = mm_to_meter(vf)


ti = float(0) 
tf = float(50) 
M =[
    [1, ti, ti**2, ti**3, ti**4, ti**5],
    [0, 1, 2*ti, 3*ti**2, 4*ti**3, 5*ti**4],
    [0, 0, 2, 6*ti, 12*ti**2, 20**ti**3],
    [1, tf, tf**2, tf**3, tf**4, tf**5],
    [0, 1, 2*tf, 3*tf**2, 4*tf**3, 5*tf**4],
    [0, 0, 2, 6*tf, 12*tf**2, 20*tf**3] 
]
M =np.matrix(M)

b =[[di],[vi],[aci],[df],[vf],[acf]]

a = np.linalg.inv(M)*b  

x = np.arange(ti, tf, 0.05)

def qt(t,c0,c1,c2,c3,c4,c5):
    return c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 + c5*t**5

y =qt(x, a[0,0], a[1,0], a[2,0], a[3,0], a[4,0], a[5,0])

plt.figure()
plt.title('Trajectory Planning d2')
plt.xlabel("time(s)") 
plt.ylabel("d2(meter)") 
plt.plot(x,y,'c',linestyle = '-')
plt.text(0.05, 0.7, 'c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 + c5*t**5')
plt.grid(True)
plt.show()