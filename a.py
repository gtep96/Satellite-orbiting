from cgitb import text
from cmath import sqrt
from turtle import color
import txaio
txaio.use_asyncio()

import vpython as vp
vp.scene.title = "Modeling the motion of satellite with the gravitational force"
vp.scene.height = 1000
vp.scene.width = 1000

G = 6.67*10**(-11) #real-world value is : G = 6.67e-11 

#Moon settings
MoonMass=7.342*10**(22) #kg #real-world value is 7.342*10**(22) kg
MoonRadius=1737.1*1000  #m  #real-world value is 1737.1 km (average)

#Satellite settings
SatMass=1 #kg #Unused for now
SatSpeed=1700  #m/s 
SatAltitude=20*1000 #m

sat = vp.sphere(pos=vp.vector(0,MoonRadius+SatAltitude,0), radius=MoonRadius/1000, color=vp.color.blue,
               mass = SatMass, vel=vp.vector(SatSpeed, 0,0), make_trail=True )

moon = vp.sphere(pos=vp.vector(0,0,0), radius=MoonRadius*0.95, color=vp.vec(0.5,0.5,0.5), #Moon size is 95% of normal for better visualization
               mass = MoonMass, vel=vp.vector(0,0,0), make_trail=False)

CaclVel=sqrt(G*MoonMass/(SatAltitude+MoonRadius)) #Calculating the First cosmic velocity (just for info)

#Infolabels and additional visualizations
infoLabelRealAlt=vp.label(align='left',text='',pos=vp.vec(100,100,0), pixel_pos=True) #Preparing label for current altitude
infoLabelRealVel=vp.label(align='left',text='',pos=vp.vec(100,70,0), pixel_pos=True) #Preparing label for current velocity
infoLabelCalcVel=vp.label(align='left',text='',pos=vp.vec(100,40,0), pixel_pos=True) #Preparing label for calculated First cosmic velocity
infoLabelCalcVel.text=('CaclVel= ' + str(round(CaclVel.real)) + ' m/s')
vscale=100
satVelocityVisualization=vp.arrow(pos=sat.pos, axis=vscale*sat.vel, color=vp.color.yellow) #Velocity visualization arrow

def gravitationalForce(p1,p2): #Calculating gravitational acceleration
    rVector = p1.pos - p2.pos
    rMagnitude = vp.mag(rVector)
    rHat = rVector / rMagnitude
    F = - rHat * G * p1.mass * p2.mass/rMagnitude**2
    return F

t = 0
dt = 1 #The step size. This should be a small number (normally 0.0001) #For faster simulation changed up to 1


while True: #Simulating
    vp.rate(50)
    
    #Calculte the force using gravitationalForce function
    moon.force = gravitationalForce(moon,sat)
    sat.force = gravitationalForce(sat,moon)
    
    #Update vel & position
    moon.vel = moon.vel + moon.force*dt
    sat.vel = sat.vel + sat.force*dt
    moon.pos = moon.pos + moon.vel/moon.mass*dt
    sat.pos = sat.pos + sat.vel/sat.mass*dt
    
    satVelocityVisualization.pos=sat.pos
    satVelocityVisualization.axis=vscale*sat.vel
    
    #Printing current altitude and velocity
    infoLabelRealAlt.text=('Alt= ' + str(round(vp.vec(sat.pos).mag - MoonRadius)) + ' m')
    infoLabelRealVel.text=('Vel= ' + str(round(vp.vec(sat.vel).mag)) + ' m/s')
        
    #Updating time
    t+= dt
    
