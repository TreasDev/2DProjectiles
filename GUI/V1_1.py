import tkinter as tk
#import matplotlib.pyplot as plt
import numpy as np
g = 9.81 #ms^-2
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    def create_widgets(self):
        #inital velocity
        self.vel_label = tk.Label(self, text="Inital Velocity [ms^-1]")
        self.vel_label.grid(row=0, column=0)
        self.vel_slider = tk.Scale(self, from_=1, to=100, orient='horizontal')
        self.vel_slider.grid(row=0, column=1)
        #angle
        self.angle_label = tk.Label(self, text="Angle [deg]")
        self.angle_label.grid(row=1, column=0)
        self.angle_slider = tk.Scale(self, from_=1, to=89, orient='horizontal')
        self.angle_slider.grid(row=1, column=1)
        #submit
        self.submit = tk.Button(self, text="calculate", command=self.calc)
        self.submit.grid(row=2, columnspan=2)
        #tof
        self.tof_label = tk.Label(self, text="Time of Flight [s]")
        self.tof_label.grid(row=3, column=0)
        self.tof_output = tk.Label(self)
        self.tof_output.grid(row=3, column=1)
        #horizontal displacement
        self.hd_label = tk.Label(self, text="Horizontal Displacement [m]")
        self.hd_label.grid(row=4, column=0)
        self.hd_output = tk.Label(self)
        self.hd_output.grid(row=4, column=1)
        #max vertical
        self.maxy_label = tk.Label(self, text="Max Vertical Displacement [m]")
        self.maxy_label.grid(row=5, column=0)
        self.maxy_output = tk.Label(self)
        self.maxy_output.grid(row=5, column=1)
    def calc(self):
        v = float(self.vel_slider.get())
        theta = float(self.angle_slider.get())*(np.pi/180)
        #tof
        t = np.sqrt((2*v*np.sin(theta))/g)
        self.tof_output.config(text="%.5e" % t)
        #hd
        x = v*np.cos(theta)*t
        self.hd_output.config(text="%.5e" % x)
        #max vertical
        maxy = ((v**2)*np.sin(theta)**2)/(2*g**2)
        self.maxy_output.config(text="%.5e" % maxy)
root=tk.Tk()
root.title("2D Projectiles")
app=App(master=root)
app.mainloop()