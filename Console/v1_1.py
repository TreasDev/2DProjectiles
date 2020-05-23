#imports
import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval
from math import pow
#vars
u = 0
ang = 0
tof = 0
xrange = 0
yrange = 0
g = 9.81
#funcs
def calc(v, angle):
    theta = np.radians(angle)
    t = (2*v*np.sin(theta))/g
    x = v*np.cos(theta)*t
    y = ((v*np.sin(theta)*t)/2)-((g*pow(t, 2))/8)
    print("Time of flight [s]: %.3e" % t)
    print("Horizontal range [m]: %.3e" % x)
    print("Vertical range [m]: %.3e" % y)
    return t, x, y
#def graph(tmax, v, angle):
#   t = np.linspace(0, tmax)
#    theta = np.radians(angle)
#    plt.plot((v*np.cos(theta)*t), (v*np.sin(theta)*t-((g*t*t)/2)))
#    plt.xlim(0)
#    plt.ylim(0)
#    plt.xlabel('Horizontal Displacement [m]')
#    plt.ylabel('Vertical Displacement [m]')
#    plt.ticklabel_format(axis='both', style='sci')
#    plt.title('Projectile Motion')
#    plt.show()
#get input
while u <= 0:
        u = literal_eval(input("Input initial velocity [ms^-1]: "))
        if u < 0:
            print("invalid value entered")
while ang < 0.01 or ang > 90:
    ang = literal_eval(input("Input angle of projection relative to the x axis [deg]: "))
    if ang < 0 or ang > 90:
        print("invalid value entered")
#output
tof, xrange, yrange = calc(u, ang)
#graph(tof, u, ang)