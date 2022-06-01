import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import matplotlib.pyplot as plt
from sqlalchemy import true

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
               mm_to_meter(float(0)),
               mm_to_meter(float(0))
               ])
q2 = np.array([deg_to_rad(float(45)),
               mm_to_meter(float(750)),
               mm_to_meter(float(0))
               ])
q3 = np.array([deg_to_rad(float(45)),
               mm_to_meter(float(750)),
               mm_to_meter(float(850))
               ])

q4= np.array([deg_to_rad(float(60)),
               mm_to_meter(float(0)),
               mm_to_meter(float(0))
               ])
q5 = np.array([deg_to_rad(float(60)),
               mm_to_meter(float(750)),
               mm_to_meter(float(0))
               ])
q6 = np.array([deg_to_rad(float(60)),
               mm_to_meter(float(750)),
               mm_to_meter(float(850))
               ])

q7 = np.array([deg_to_rad(float(-90)),
               mm_to_meter(float(0)),
               mm_to_meter(float(0))
               ])
q8 = np.array([deg_to_rad(float(-90)),
               mm_to_meter(float(750)),
               mm_to_meter(float(0))
               ])
q9 = np.array([deg_to_rad(float(-90)),
               mm_to_meter(float(750)),
               mm_to_meter(float(850))
               ])
q10 = np.array([deg_to_rad(float(-45)),
               mm_to_meter(float(0)),
               mm_to_meter(float(0))
               ])
q11 = np.array([deg_to_rad(float(-45)),
               mm_to_meter(float(750)),
               mm_to_meter(float(0))
               ])
q12 = np.array([deg_to_rad(float(-45)),
               mm_to_meter(float(750)),
               mm_to_meter(float(850))
               ])
          

# Trajectory commands
traj1 = rtb.jtraj(q0,q1,5)
traj2 = rtb.jtraj(q1,q2,5)
traj3 = rtb.jtraj(q2,q3,5)
traj4 = rtb.jtraj(q3,q2,5)
traj3_return = rtb.jtraj(q2,q1,5)
traj2_return = rtb.jtraj(q1,q4,5)
traj1_2= rtb.jtraj(q4,q5,5)
traj2_2= rtb.jtraj(q5,q6,5)
traj3_2= rtb.jtraj(q6,q5,5)
traj3_2return= rtb.jtraj(q5,q4,5)
traj2_2return= rtb.jtraj(q4,q7,5)
traj1_3= rtb.jtraj(q7,q8,5)
traj2_3= rtb.jtraj(q8,q9,5)
traj3_3= rtb.jtraj(q9,q8,5)
traj3_3return= rtb.jtraj(q8,q7,5)
traj2_3return= rtb.jtraj(q7,q10,5)
traj1_3return= rtb.jtraj(q10,q11,5)
traj1_4= rtb.jtraj(q11,q12,5)
traj2_4= rtb.jtraj(q12,q11,5)
traj3_4= rtb.jtraj(q11,q10,5)
traj1_1= rtb.jtraj(q10,q0,5)

Cyl_Standard.plot(traj1.q)
Cyl_Standard.plot(traj2.q)
Cyl_Standard.plot(traj3.q)
Cyl_Standard.plot(traj3_return.q)
Cyl_Standard.plot(traj2_return.q)
Cyl_Standard.plot(traj1_2.q)
Cyl_Standard.plot(traj2_2.q)
Cyl_Standard.plot(traj3_2.q)
Cyl_Standard.plot(traj3_2return.q)
Cyl_Standard.plot(traj2_2return.q)
Cyl_Standard.plot(traj1_3.q)
Cyl_Standard.plot(traj2_3.q)
Cyl_Standard.plot(traj3_3.q)
Cyl_Standard.plot(traj3_3return.q)
Cyl_Standard.plot(traj2_3return.q)
Cyl_Standard.plot(traj1_3return.q)
Cyl_Standard.plot(traj1_4)
Cyl_Standard.plot(traj2_4)
Cyl_Standard.plot(traj3_4)
Cyl_Standard.plot(traj1_1, block=True)