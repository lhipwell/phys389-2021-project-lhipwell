import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import matplotlib.cm as cm

m1=1#the mass of the inner pendulum(changable)
m2=1#the mass of the outer pendulum(changable)

r1=1#the radius of the inner pendulum from the origin(changable) 
r2=1#the radius of the outer pendulum from the origin(changable)

counter =1#defining this to set up a while loop that will lopp the simulation for new input angles

data=[]# start this array to store data in later

starttheta1=0#the angular velocity of the inner pendulum(counter clockwise is defined as positive)  
starttheta2=0#the angular velocity of the outer pendulum(counter clockwise is defined as positive)

while counter ==1:
    counter2=1#defining tthis for a while loop that runs the simulation
    theta1=starttheta1#the value of theta's will be changed but the system need to know the starting angle  
    theta2=starttheta2
    theta11=0#this is the angle of the inner pendulum for the first simulation
    theta21=0#this is the angle of the outer pendulum for the first simulation
    loop='false'# this is the variable to determine if the system has flipped 
    time=0#each simulation should start at 0 time
    deltaT=0.001# how often the system will update variables (seconds)
    while counter2==1:
        a=(m1+m2)*r1#these are the variables used in the langrange equation so it was easier to understand the equation broken down like this
        b=m2*r2*math.cos((theta1-theta2)%(2*math.pi))#it also means that these values only have to be calculated once but can be used multiple times 
        c=m2*r1*math.cos((theta1-theta2)%(2*math.pi))#for example in lines 37 and 38
        d=m2*r2
        e=-m2*r2*theta21*theta21*math.sin((theta1-theta2)%(2*math.pi))-(m1+m2)*9.81*math.sin(theta1%(2*math.pi))
        f=m2*r1*theta11*theta11*math.sin((theta1-theta2)%(2*math.pi))-m2*9.81*math.sin(theta2%(2*math.pi))
        theta12=(e*d-b*f)/(a*d-b*c)#this is the lagrange equation to calulcate the angular acceleration of the inner pendulum
        theta22=(a*f-c*e)/(a*d-b*c)#this is the lagrange equation to calulcate the angular acceleration of the outer pendulum   
        theta11+=theta12*deltaT#Euler approxiation calculation for calculating the angular velocity of the inner pendulum
        theta21+=theta22*deltaT#Euler approxiation calculation for calculating the angular velocity of the outer pendulum
        theta1+=theta11*deltaT#Euler approxiation calculation for calculating the angular position of the inner pendulum
        theta2+=theta21*deltaT#Euler approxiation calculation for calculating the angular position of the outer pendulum
        angle=theta2#this will be important as angle should only be defined between 0 and 2pi but mulitple flips will make the exceed the expected range 
        if angle>=2*math.pi or angle<0 :#this means that angle will only be be between 0 and 2pi without effecting the simulation that uses the theta variable
            angle=angle%(2*math.pi)
        if (angle<=math.pi-0.01 or angle>=math.pi+0.01)and loop=='false': #this is so that when the starting angle is roughly pi the flip checks will not automatically pass  
            loop='start'    
        if angle>=math.pi-0.01 and angle<=math.pi+0.01 and loop=='start':#making sure the pendulum passes through the upwards vertical position
            loop='true'
        if loop=='true'and angle<=starttheta2+0.01 and angle>=starttheta2-0.01:# checking the pendulum passes back to the starting position (the partcile may pass the exact position between checks thus there is a range the position must fall between)
            counter2=2# this stops the loop of the current simulation 
            data.append([starttheta1, starttheta2, time])#appending the data to the data array 
        if time>10000: # this is the cut off time as if there was insuffient energy in the system (and thus doesnt flip) the simulate would run forver 
            data.append([starttheta1, starttheta2, time]) #appending the data to the data array 
            counter2=2# this stops the loop of the current simulation
        time+=deltaT# this updates the curent time in the system
    print('theta1:', starttheta1, 'theta2:', starttheta2 )#this indicates the current simulation to the user 
    starttheta1+=0.1#the next simulation will start with an increased theta1 angle
    if starttheta1>2*math.pi:#if the internal angle is larger than 2 pi then the system should be the same so increase the out pendulum angle then start again
        starttheta2+=0.1
        starttheta1=0
    if starttheta2>2*math.pi:# if the outer pendulum angle has done the full loop then the all starting angles have been tested
        counter=2#stops the loop of the simulations to stop the program
df=pd.DataFrame(data, columns=['Theta1', 'Theta2', 'Time'])# arranges the data collected into a dataframe
df.to_csv('Output_Data1.csv') #this saves the dataframe to an extrernal file or to be graphed with the graphing program 
