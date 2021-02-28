import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from Particle5 import Particle


#these are the characteristic about the pendulums which can be altered
firstMass = 1 
firstPosition = [1,0]  # system center is defined at 0,0
firstVelocity = [0,10] 

#please dont alter these as they are characteristics of the system determined by the above variables
firstRadius = np.linalg.norm(firstPosition) 
firstAngle = math.asin(firstPosition[0]/firstRadius)
first = Particle(firstPosition, firstVelocity, [0,0], 'first', firstMass, firstRadius, firstAngle) # using the class particle from file particle5 to "link" these characteristic together 


deltaT=0.00001#how often the system variables are updated
time=10#how long the sysetm will simulate

#use array to store data on all positions so they can be plotted
first.xaxis=[]
first.yaxis=[]

#determines the forces acting on a partcile
def force(self,deltaT):
    weight=self.mass*9.81
    self.force[0]=tension(self)*(-1*math.sin(self.angle)) #minus sign due to if partcile is on right the acceleration is left
    self.force[1]=-weight+tension(self)*math.cos(self.angle) #weight is "down" in this system so needs a minus sign


#determines the tension experienced by the particle 
def tension(self):
    perpvelocity= (2*(totenergy-potentialenergy(self))/self.mass)**(1/2) 
    centripital=(self.mass/self.radius)*perpvelocity**2
    tension=centripital+self.mass*9.81*math.cos(self.angle)
    return tension

#calculates the kinetic energy of the particle
def kineticenergy(self):
    kinetic = 0.5*self.mass*(np.linalg.norm(self.velocity))**2 
    return kinetic

#calculates the potential energy of the partcile
def potentialenergy(self):
    potential = self.mass*(self.position[1]+self.radius)*9.81
    return potential

#calcultes the total energy of a particle
def totalenergy(self):
    total=kineticenergy(self)+potentialenergy(self)
    return total


for i in range(int(time/deltaT)+1):
    if i==0:
        totenergy=totalenergy(first)#used to make sure that energy is conserved/ doesnt vary
    if totenergy<=potentialenergy(first):#was having problem with teh potential energy being larger than total energy due to rounding errors
        totenergy=potentialenergy(first)
    force(first,deltaT)#updates the forces eperienced by the particle
    first.update(deltaT)#uses the forces to calculate the accerleration, velocity, poitsion and angle with respect to origin
    first.xaxis.append(first.position[0])#adds current postion to the end of array
    first.yaxis.append(first.position[1])
 

            #if save=="yes":
             #   tosave.append(self.position[0])
              #  tosave.append(self.position[1])
    


#plots the positions of the particles 
plt.plot(first.xaxis, first.yaxis)

#shows the plots
plt.show()

