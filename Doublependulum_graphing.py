import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm
from matplotlib.colors import LogNorm

df = pd.read_csv('Output_Data3.csv', index_col=0).to_numpy() #this loads the saved data from the simulation file and makes it a numpy array  

data=np.zeros(shape=(int(len(df)**0.5),int(len(df)**0.5)))# this creates a large empty array so that the values of time can be inserted to form the graph
g=0#this is setting up counters to use in the for loop
n=0
for i in range(0,int(len(df))):#this should loop should repeat for every value in the dataframe
    data[n][g]=df[i][2]#this allocates the value specificed in the data frame a new location in the numpy aray to be graphed
    g+=1
    if g==int(len(df)**0.5):#This is so when the end of the row has been reached the code will select the start of the row
        n+=1
        g=0

plt.xlabel('Starting angle of inner pendulum(Radians)',fontsize=8)#These are the labels on the x and y axes to be plotted
plt.ylabel('Starting angle of outer pendulum(Radians)',fontsize=8)
plt.imshow(data, extent=[0,2*math.pi,0,2*math.pi], norm=LogNorm(), cmap=cm.magma, aspect='auto', interpolation='none')#This constructs the graph from the data nunmpy array 
plt.colorbar() #Shows that the colour bar at the right of the graph should be shown 
plt.title('Double pendulum flip time dependance on starting angles',fontsize=8)# this is the title of the graph
plt.show()#this outputs the graph plotted

