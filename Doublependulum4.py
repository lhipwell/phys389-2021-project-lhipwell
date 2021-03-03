import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from Particles import Particle

firstMass = 1 
firstPosition = [1,0]  # system center is defined at 0,0
firstVelocity = [0,0] 
firstRadius = np.linalg.norm(firstPosition)
firstAngle = math.asin(firstPosition[0]/firstRadius)
first = Particle(firstPosition, firstVelocity, [0,0], 'first', firstMass, firstRadius, firstAngle) 

secondMass = 1 
secondPosition = [2,0] 
secondVelocity = [0,0] 
secondRadius = ((secondPosition[0]-firstPosition[0])**2+(secondPosition[1]-firstPosition[1])**2)**0.5
secondAngle = math.asin((((secondPosition[0]-firstPosition[0])**2+(secondPosition[1]-firstPosition[1])**2)**0.5)/secondRadius)
second = Particle(secondPosition, secondVelocity, [0,0], 'second', secondMass, secondRadius, secondAngle) 



deltaT=0.01
time=10


first.xaxis=[]
first.yaxis=[]
second.xaxis=[]
second.yaxis=[]


def update1(self, deltaT):
    g=1
    for i in range (0,2):
        self.acceleration[i] = self.force[i]/self.mass
        self.velocity[i] = self.velocity[i] + (self.acceleration[i]*deltaT)
        self.position[i] = self.position[i] + (self.velocity[i]*deltaT)
        if np.linalg.norm(self.position)!=self.radius:
            self.position[i]= self.position[i]*self.radius/np.linalg.norm(self.position)             
    if self.position[1]>0.001:
        self.angle=math.pi+math.atan(-self.position[0]/self.position[1])
    if self.position[1]<0.001:
        self.angle=math.atan(-self.position[0]/self.position[1])
    if first.position[1]<=0.001 and first.position[1]>=-0.001:
        angle=(first.position[0]/self.radius)
        while g==1:
            if angle>1:
                angle-=2
            if angle<-1:
                angle+=2
            else:
                g=2
        self.angle= math.asin(angle) 
        g=1



def update2(self, deltaT):
    g=1
    for i in range (0,2):
        self.acceleration[i] = self.force[i]/self.mass
        self.velocity[i] = self.velocity[i] + (self.acceleration[i]*deltaT)
        self.position[i] = self.position[i] + (self.velocity[i]*deltaT)
        if ((second.position[0]-first.position[0])**2+(second.position[1]-first.position[1])**2)**0.5 !=self.radius:
            self.position[i]= self.position[i]*self.radius/((second.position[0]-first.position[0])**2+(second.position[1]-first.position[1])**2)**0.5            
    if second.position[1]-first.position[1]>0.001:
        self.angle=math.pi+math.atan(-(second.position[0]-first.position[0])/(second.position[1]-first.position[1]))
    if second.position[1]-first.position[1]<0.001:
        self.angle=math.atan(-(second.position[0]-first.position[0])/(second.position[1]-first.position[1]))
    if second.position[1]-first.position[1]<=0.001 and second.position[1]-first.position[1]>=-0.001:
        angle=(second.position[0]-first.position[0]/self.radius)
        while g==1:
            if angle>1:
                angle-=2
            if angle<-1:
                angle+=2
            else:
                g=2
        self.angle= math.asin(angle) 
        g=1


def force1(self,deltaT): 
    weight=self.mass*9.81
    self.force[0]=tension1(self)*(-1*math.sin(self.angle))+tension2(second)*(-1*math.sin(second.angle))
    self.force[1]=-weight+tension1(self)*math.cos(self.angle)+tension2(second)*math.cos(second.angle)

def force2(self,deltaT): 
    weight=self.mass*9.81
    self.force[0]=tension2(self)*(-1*math.sin(self.angle))
    self.force[1]=-weight+tension2(self)*math.cos(self.angle)
    


def tension1(self):
    perpvelocity= (2*(totenergy-(potentialenergy2(first)+potentialenergy2(second)+kineticenergy(second))/self.mass))**(1/2) 
    centripital= (self.mass/self.radius)*perpvelocity**2
    tension=centripital+self.mass*9.81*math.cos(self.angle)+tension2(second)*math.cos(first.angle-second.angle)#changed cos to sin 
    return tension

def tension2(self):
    perpvelocity= (2*(totenergy-(potentialenergy2(first)+potentialenergy2(second)+kineticenergy(first))/self.mass))**(1/2) 
    centripital= (self.mass/self.radius)*perpvelocity**2
    tension=centripital+self.mass*9.81*math.cos(self.angle)
    return tension

def kineticenergy(self):
    kinetic = 0.5*self.mass*(np.linalg.norm(self.velocity))**2 
    return kinetic

#def potentialenergy1(self):
 #   potential = self.mass*(self.position[1]+self.radius)*9.81
  #  return potential

def potentialenergy2(self):
    potential = self.mass*(self.position[1]+first.radius+second.radius)*9.81
    return potential

#def totalenergy1(self):
 #   total=kineticenergy(self)+potentialenergy1(self)
  #  return total

def totalenergy2(self):
    total=kineticenergy(self)+potentialenergy2(self)
    return total

for i in range(int(time/deltaT)+1):
    if i==0:
        totenergy=totalenergy2(first)+totalenergy2(second)
    if totenergy<=(potentialenergy2(first)+potentialenergy2(second)):
        totenergy=(potentialenergy2(first)+potentialenergy2(second))
    force2(second,deltaT)
    force1(first,deltaT)
    update1(first,deltaT)
    first.xaxis.append(first.position[0])
    first.yaxis.append(first.position[1])
    update2(second,deltaT)
    second.xaxis.append(second.position[0])
    second.yaxis.append(second.position[1])
    #print(first.force,'1')
    #print(second.force,'2')
    print(totalenergy2(first)+totalenergy2(second))
 
    



plt.plot(first.xaxis, first.yaxis)
plt.plot(second.xaxis, second.yaxis)


#plt.show()

