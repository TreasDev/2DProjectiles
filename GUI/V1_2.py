import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#import webbrowser
#from tkhtmlview import HTMLLabel
#def vars
g = 9.81 #[ms^-2]
#def funcs
window = tk.Tk()
window.geometry("1280x720")
#window.iconphoto(False, tk.PhotoImage(file=r'icon.png'))
window.title('Projectiles')
#input
u_label = tk.Label(window, text="Initial Velocity [ms^-1]: ").grid(row=0, column=0, padx=10, pady=15)
u_input = tk.Scale(window, from_=0.1, to=100, resolution=0.1, orient='horizontal')
u_input.grid(row=0, column=1)
angle_label = tk.Label(window, text="Angle [deg]: ").grid(row=1, column=0)
angle_input = tk.Scale(window, from_=0.1, to=89, resolution=0.1, orient='horizontal')
angle_input.grid(row=1, column=1, padx=10, pady=15)
#calc func
def plotgraph():
    u = float(u_input.get())
    theta = float(angle_input.get())*(np.pi/180)
    #tof
    tof = (2*u*np.sin(theta))/g
    tof_output.config(text="%.5e" % tof)
    #hd
    x = u*np.cos(theta)*tof
    hd_output.config(text="%.5e" % x)
    #max vertical
    maxvert = ((u**2)*np.sin(theta)**2)/(2*g**2)
    maxvert_output.config(text="%.5e" % maxvert)
    t = np.linspace(0, tof)
    f = Figure()
    fig = f.add_subplot(111)
    fig.plot((u*np.cos(theta)*t), (u*np.sin(theta)*t - (g*t*t)/2))
    fig.set_ylim(bottom=0)
    fig.set_xlim(left=0)
    fig.set_ylabel('Vertical Displacement [m]')
    fig.set_xlabel('Horizontal Displacement [m]')
    canvas = FigureCanvasTkAgg(f, window)
    canvas.draw()
    canvas.get_tk_widget().grid(column=3, row=0, columnspan=4, rowspan=6, padx = 10, pady = 10)
    #plt.show(fig)
#calculation button
calc_butt = tk.Button(window, text="calculate", command=plotgraph).grid(row=2, column=0, columnspan=2, pady=15)
#output
tof_label = tk.Label(window, text="Time of Flight [s]: ").grid(row=3, column=0, padx= 10, pady=15)
tof_output = tk.Label(window)
tof_output.grid(row=3, column=1)
hd_label = tk.Label(window, text="Horizontal Displacement [m]: ").grid(row=4, column=0, padx=10, pady=15)
hd_output = tk.Label(window)
hd_output.grid(row=4, column=1)
maxvert_label = tk.Label(window, text="Max vertical displacement [m]: ").grid(row=5, column=0, padx=10, pady=15)
maxvert_output = tk.Label(window)
maxvert_output.grid(row=5, column=1)
#graphs
f = Figure()
fig = f.add_subplot(111)
#fig.plot((u*np.cos(theta)*t), (u*np.sin(theta)*t - (g*t*t)/2))
fig.set_ylim(bottom=0)
fig.set_xlim(left=0)
fig.set_ylabel('Vertical Displacement [m]')
fig.set_xlabel('Horizontal Displacement [m]')
canvas = FigureCanvasTkAgg(f, window)
canvas.draw()
canvas.get_tk_widget().grid(column=3, row=0, columnspan=4, rowspan=6, padx = 10, pady = 10)
#branding
#name_label = HTMLLabel(window, html='<link rel="stylesheet" href="styles.css">Alex Healey, <a href= "https://treasdev.github.io/" style="text-decoration: none; color: black;">Treas Dev</a>, 2020, V1.2').grid(row=6, column=4)
#def link():
#    webbrowser.open_new("https://treasdev.github.io/")
link_label = tk.Label(window, text="Alex Healey, Treas Dev, 2020, V1.2")
link_label.grid(row=6, column=4)
#link_label.bind("<Button-1>", lambda e: link())
#run app
window.mainloop()
input() #get log output