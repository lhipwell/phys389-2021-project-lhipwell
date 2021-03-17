import math

def potentialenergy(m1,m2,theta1,theta2,r1,r2):
    penergy=9.81*((m1+m2)*r1*math.cos(theta1)+m2*r2*math.cos(theta2))
    return(penergy)

def kineticenergy(m1,m2,r1,r2,theta1,theta2,theta11,theta21):
    kenergy=0.5*(m1+m2)*(r1**2)*(theta11**2)+0.5*m2*(r2**2)*(theta21**2)+m2*r1*r2*theta11*theta21*math.cos(theta1-theta2)
    return(kenergy)

def totalenergy(m1,m2,r1,r2,theta1,theta2,theta11,theta21):
    tenergy=potentialenergy(m1,m2,theta1,theta2,r1,r2)+kineticenergy(m1,m2,r1,r2,theta1,theta2,theta11,theta21)
    return(tenergy)

if potentialenergy(1,1,math.pi,math.pi,1,1)==-29.43:
    print('Passed')
if kineticenergy(1,1,1,1,math.pi,math.pi,0,0)==0:
    print('Passed')
if kineticenergy(1,1,1,1,math.pi,math.pi,1,1)==2.5:
    print('Passed')
if totalenergy(1,1,1,1,math.pi,math.pi,0,0)==-29.43:
    print('Passed')
if totalenergy(1,1,1,1,math.pi,math.pi,1,1)==-26.93:
    print('Passed')