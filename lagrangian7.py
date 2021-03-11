import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import matplotlib.cm as cm

m1=1
m2=1

r1=1
r2=1
#angles(radians) are measured from "down" /the -y direction, math.pi command will be useful
counter =1

data=[]

starttheta1=0
starttheta2=0

while counter ==1:
    counter2=1
    theta1=starttheta1
    theta2=starttheta2
    theta11=0
    theta21=0
    loop='false'
    time=0
    deltaT=0.001
    while counter2==1:
        a=(m1+m2)*r1
        b=m2*r2*math.cos((theta1-theta2)%(2*math.pi))
        c=m2*r1*math.cos((theta1-theta2)%(2*math.pi))
        d=m2*r2
        e=-m2*r2*theta21*theta21*math.sin((theta1-theta2)%(2*math.pi))-(m1+m2)*9.81*math.sin(theta1%(2*math.pi))
        f=m2*r1*theta11*theta11*math.sin((theta1-theta2)%(2*math.pi))-m2*9.81*math.sin(theta2%(2*math.pi))
        theta12=(e*d-b*f)/(a*d-b*c)
        theta22=(a*f-c*e)/(a*d-b*c)   
        theta11+=theta12*deltaT
        theta21+=theta22*deltaT
        theta1+=theta11*deltaT
        theta2+=theta21*deltaT 
        angle=theta2
        if angle>=2*math.pi or angle<0 :
            angle=angle%(2*math.pi)
        if (angle<=math.pi-0.01 or angle>=math.pi+0.01)and loop=='false': 
            loop='start'    
        if angle>=math.pi-0.01 and angle<=math.pi+0.01 and loop=='start':
            loop='true'
        if loop=='true'and angle<=starttheta2+0.01 and angle>=starttheta2-0.01:  
            counter2=2
            data.append([starttheta1, starttheta2, time])
        if time>10000:
            data.append([starttheta1, starttheta2, time]) 
            counter2=2
        time+=deltaT
    print('theta1:', starttheta1, 'theta2:', starttheta2 )
    starttheta1+=0.1
    if starttheta1>2*math.pi:
        starttheta2+=0.1
        starttheta1=0
    if starttheta2>2*math.pi:
        counter=2
df=pd.DataFrame(data, columns=['Theta1', 'Theta2', 'Time'])
df.to_csv('Output_Data1.csv')
