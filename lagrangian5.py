import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

m1=1
m2=1

r1=1
r2=1
#angles(radians) are measured from "down" /the -y direction, math.pi command will be useful
#counter =1
#while counter ==1:
counter2=1
starttheta1=math.pi
starttheta2=math.pi-0.1
theta1=math.pi
theta2=math.pi-0.001
theta11=0
theta21=0
loop='false'

time=0
deltaT=0.01
#totaltime=40

firstx=[]
firsty=[]
secondx=[]
secondy=[]

x1=0
y1=0
x2=0
y2=0

while counter2==1:
    a=(m1+m2)*r1
    b=m2*r2*math.cos(theta1-theta2)
    c=m2*r1*math.cos(theta1-theta2)
    d=m2*r2
    e=-m2*r2*theta21*theta21*math.sin(theta1-theta2)-(m1+m2)*9.81*math.sin(theta1)
    f=m2*r1*theta11*theta11*math.sin(theta1-theta2)-m2*9.81*math.sin(theta2)
    theta12=(e*d-b*f)/(a*d-b*c)
    theta22=(a*f-c*e)/(a*d-b*c)   
    theta11+=theta12*deltaT
    theta21+=theta22*deltaT
    theta1+=theta11*deltaT
    theta2+=theta21*deltaT 
    #x1=r1*math.sin(theta1)
    #y1=-r1*math.cos(theta1)
    #x2=x1+r2*math.sin(theta2)
    #y2=y1-r2*math.cos(theta2)
    #firstx.append(x1)
    #firsty.append(y1)
    #secondx.append(x2)
    #secondy.append(y2)
    if (theta1<=math.pi-0.001 and theta1>=math.pi+0.001)and loop=='false': #changed first and from an or
        loop='start'
        if theta11>=0:
            startvel='+'
            print('1')
        else:
            startvel='-'
            print('1')
    if theta1>=math.pi-0.001 and theta1<=math.pi+0.001 and loop=='start':
        loop='true'
        print('2')
    if loop=='true'and theta1<=starttheta1+0.001 and theta1>=starttheta1-0.001:
            print('3')
            if (startvel=='+' and theta11>0) or (startvel=='-' and theta11<0):
                print(time)
                counter2=2
                #save time and restart with new start angles
    time+=deltaT
    

#plt.plot(firstx, firsty)
#plt.plot(secondx, secondy)
#plt.show()