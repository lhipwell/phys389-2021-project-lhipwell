import math
import matplotlib.pyplot as plt
import numpy as np

#this system assumes massless rigid rods, no air reisitance, pointlike particiles of the pendulum masses, no dampening to the system and experiences uniform gravitation field (which was a strength of 9.81ms-1)   

#customisable variables

m1=1 #mass of the internal pendulum
m2=1 #mass of the external pendulum

r1=1 #radius of the internal pendulum (from the origin) 
r2=1 #radius of the external pendulum (from the internal pendulum)
#angles(radians) are measured from "down" /the -y direction, math.pi command will be useful
theta1=math.pi #start angle of the internal pendulum (pendulum 1)
theta2=math.pi/2 #start angle of the external pendulum (pendulum 2)
theta11=0 #angular velocity of the internal pendulum
theta21=0 #angular velocity of the external pendulum

time=0 #start time
deltaT=0.01 #the time between system updates
totaltime=40 #how long to simulate the system for

#dont change variables from here down

firstx=[]#will be an array of all the inner pendulum x coordinates
firsty=[]#will be an array of all the inner pendulum y coordinates
secondx=[]#will be an array of all the outer pendulum x coordinates
secondy=[]#will be an array of all the outer pendulum y coordinates

x1=0#will be used as a place holder for the current x position of internal pendulum
y1=0#will be used as a place holder for the current y position of internal pendulum
x2=0#will be used as a place holder for the current x position of external pendulum
y2=0#will be used as a place holder for the current y position of external pendulum

for i in range(int((totaltime/deltaT)+1)): #the loop will reccur and is when the system updates  
    a=(m1+m2)*r1#these are the variables used in the langrange equation so it was easier to understand the equation broken down like this  
    b=m2*r2*math.cos((theta1-theta2)%(2*math.pi))#it also means that these values only have to be calculated once but can be used multiple times 
    c=m2*r1*math.cos((theta1-theta2)%(2*math.pi))
    d=m2*r2
    e=-m2*r2*theta21*theta21*math.sin((theta1-theta2)%(2*math.pi))-(m1+m2)*9.81*math.sin(theta1%(2*math.pi))
    f=m2*r1*theta11*theta11*math.sin((theta1-theta2)%(2*math.pi))-m2*9.81*math.sin(theta2%(2*math.pi))
    theta12=(e*d-b*f)/(a*d-b*c)#this is the lagrange equation to calulcate the angular acceleration of the inner pendulum 
    theta22=(a*f-c*e)/(a*d-b*c)#this is the lagrange equation to calulcate the angular acceleration of the outer pendulum   
    theta11+=theta12*deltaT#Euler approxiation calculation for calculating the angular velocity of the inner pendulum 
    theta21+=theta22*deltaT#Euler approxiation calculation for calculating the angular velocity of the outer pendulum
    theta1+=theta11*deltaT#Euler approxiation calculation for calculating the angular position of the inner pendulum
    theta2+=theta21*deltaT #Euler approxiation calculation for calculating the angular position of the outer pendulum
    x1=r1*math.sin(theta1)#using the angle to calculate the x position of the inner pendulum
    y1=-r1*math.cos(theta1)#using the angle to calculate the y position of the inner pendulum
    x2=x1+r2*math.sin(theta2)#using the angle to calculate the x position of the outer pendulum
    y2=y1-r2*math.cos(theta2)#using the angle to calculate the y position of the outer pendulum
    firstx.append(x1)#adding the current x position of the inner pendulum to the array of the previous x positions 
    firsty.append(y1)#adding the current y position of the inner pendulum to the array of the previous y positions
    secondx.append(x2)#adding the current x position of the outer pendulum to the array of the previous x positions
    secondy.append(y2)#adding the current y position of the outer pendulum to the array of the previous y positions
    time+=deltaT#This is the counting the 'current' time of the system

plt.plot(firstx, firsty)#plotting the positions of the inner pendulum 
plt.plot(secondx, secondy)#plotting the positions of the outer pendulum
plt.show()#shows the graph of all the positions of both particiles 