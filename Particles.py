import numpy as np
import math

class Particle:
    def __init__(self, Position=np.array([0,0], dtype=float), Velocity=np.array([0,0], dtype=float), Acceleration=np.array([0,0], dtype=float), Name='Ball', Mass=1.0, radius=1.0, Angle=1.0, force =np.array([0,0], dtype=float) ):
        self.position = np.array(Position, dtype=float)
        self.velocity = np.array(Velocity, dtype=float)
        self.acceleration = np.array(Acceleration, dtype=float)    
        self.radius = radius
        self.Name = Name
        self.mass = Mass
        self.angle = Angle
        self.force = np.array(force, dtype=float)


    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Radius: {5}, Angle: {6}, Force: {7}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration,self.radius,self.angle, self.force)

    #def update(self, deltaT):
     #   for i in range (0,2):
      #      self.acceleration[i] = self.force[i]/self.mass
       #     self.velocity[i] = self.velocity[i] + (self.acceleration[i]*deltaT)
        #    self.position[i] = self.position[i] + (self.velocity[i]*deltaT)
         #   if np.linalg.norm(self.position)!=self.radius:
          #      self.position[i]= self.position[i]*self.radius/np.linalg.norm(self.position)
    #    if self.position[1] <=0.001 and self.position[1] >=-0.001: 
     #       self.angle=self.position[0]/self.position[1]  #small angle aproximations
      #  if self.position[1]>0.001:
       #     self.angle=math.pi+math.atan(-self.position[0]/self.position[1])
        #if self.position[1]<0.001:
         #   self.angle=math.atan(-self.position[0]/self.position[1])
        

      
      