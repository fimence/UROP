#from 20181227version
#math part is done!
#this version is for control UI

import math
from vpython import *
scene.width = 700
scene.height = 700
scene.title = 'THREE BODY PROBLEM(ver.1228)\n by Fimence'
scene.autoscale = True
scene.fullscreen = True

"""Controling part by ButtonsSlidersMenus-VPython""" 
running = True

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"

button(text="Pause", pos=scene.title_anchor, bind=Run)



#Speed control.Adopt from ButtonsSlidersMenus-VPython
scene.caption = "\nspeed: \n"
def speed(s):
    wt.text = '{:1.2f}'.format(s.value)    
sl = slider(min=0, max=10, value=1, length=400, bind=speed, right=15)
wt = wtext(text='{:1.2f}'.format(sl.value))
#upper part is fine



#math problems
x1 = -3
y1 = 0
x2 = 0
y2 = 0
x3 = 3
y3 = 0

k = 3
dt = 0.0001

m1 = 3
m2 = 3
m3 = 3

v1x = 0
v1y = 1
v2x = 0
v2y = 3
v3x = 0
v3y = -1


#Initial positions
pos1 = vector(x1, y2, 0) #red ball
pos2 = vector(x2, y2, 0) #green ball
pos3 =vector(x3, y3, 0) #blue ball


#velocitats inicials
v1= vector(v1x, v1y, 0) #red
v2 = vector(v2x, v2y, 0) #green
v3 = vector(v3x, v3y, 0) #blue

#DRAWING(part of the code from 3BP.py by Oriol Frigola)
d1 = pow(m1, 1./3)*0.1*0.3
d2 = pow(m2, 1./3)*0.1*0.3
d3 = pow(m3, 1./3)*0.1*0.3#change the size of the objects by change 0.3 in the last parameters
P1 = sphere(pos = pos1, radius = d1, color = color.red,make_trail=True,trail_radius=0.5*d1)
P2 = sphere(pos = pos2, radius = d2, color = color.green,make_trail=True,trail_radius=0.5*d2)
P3 = sphere(pos = pos3, radius = d3, color = color.blue,make_trail=True,trail_radius=0.5*d3)



while True:
	rate(600*sl.value)
	if running:
	#distent of 1 and 2 name as r12 
		r12x=x2-x1
		r12y=y2-y1
		r12=((r12x)**2+(r12y)**2)**0.5

	#distent of 2 and 3 name as r23
		r23x=x3-x2
		r23y=y3-y2
		r23=((r23x)**2+(r23y)**2)**0.5

	#distent of 1 and 3 name as r13
		r13x=x3-x1
		r13y=y3-y1
		r13=((r13x)**2+(r13y)**2)**0.5	

	#force between 12 body
		f12x= k * m2 * m1*r12x/r12**3
		f12y= k * m2 * m1*r12y/r12**3

	#force between 23 body
		f23x= k * m2 * m3*r23x/r23**3
		f23y= k * m2 * m3*r23y/r23**3

	#force between 13 body
		f13x= k * m3 * m1*r13x/r13**3
		f13y= k * m3 * m1*r13y/r13**3

	#speed and location of object 1
		"""Force change accraction the acceration change speed,and speed change location"""
		v1x+=f12x/m1*dt+f13x/m1*dt
		v1y+=f12y/m1*dt+f13y/m1*dt
		x1+=v1x*dt
		y1+=v1y*dt

	#speed and location of object 2
		v2x+=-f12x/m2*dt+f23x/m2*dt
		v2y+=-f12y/m2*dt+f23y/m2*dt
		x2+=v2x*dt
		y2+=v2y*dt

	#speed and location of object 3
		v3x+=-f13x/m2*dt-f23x/m2*dt
		v3y+=-f13y/m2*dt-f23y/m2*dt
		x3+=v3x*dt
		y3+=v3y*dt

		P1.pos = vector(x1, y1, 0)
		P2.pos = vector(x2,y2,0)
		P3.pos = vector(x3,y3,0)
		scene.center = vector(0,0,0)


		if r12<d1+d2 or r23<d3+d2 or r13<d3+d1: #collision
			print ("Done!")
			break


print ("...finish")





