import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import matplotlib.pyplot as plt

# link lengths in cm
a1 = float(500) # For testing, 50 cm
a2 = float(600) # For testing, 50 cm
a3 = float(700) # For testing, 40 cm

# link converted to meters
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)

# link limits converted to meters
lm2 = float(550) # 50mm
lm2 = mm_to_meter(lm2)

lm3 = float(650) # 40mm
lm3 = mm_to_meter(lm3)

# Create Links
# [robot variable]=DHRobot([RevoluteDH(d,r/a,alpha,offset)])
#PrismaticDH(theta,r,alpha,offset)
Cyl_Standard = DHRobot([
    RevoluteDH(a1,0,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH((270/180)*np.pi,0,(270/180)*np.pi,a2,qlim=[0, lm2]),
    PrismaticDH(0,0,0,a3,qlim=[0, lm3]),
], name='Cylindrical')

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi


# q Paths
q0 = np.array([0,0,0])
q1 = np.array([deg_to_rad(float(45)),
               mm_to_meter(float(550)),
               mm_to_meter(float(650))
               ])

# Trajectory commands
traj1 = rtb.jtraj(q0,q1,50)

Cyl_Standard.plot(traj1.q, block=True)

