from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk  
import numpy as np
import serial as sr 
import time
import os
import datetime
import collections
from matplotlib.lines import Line2D 

t = datetime.datetime.now()
nama_file = t.strftime("%Y_%m_%d_%H_%M_%S") 

#SET Serial Port
serial_port = sr.Serial('COM5',115200); 
serial_port.reset_input_buffer()

Samples = 50
sampleTime = 1 
numData = 2
cond = False 

#Plot Data 
def plot_data(): 
    global cond 
    waktu=time.time()
#Membuat Datasave
    outf = open(nama_file+'.csv',"a") 
    if os.stat(nama_file+'.csv').st_size == 0:
        outf.write("Times;Data 1;Data 2\n")
    

    if (cond == True): 
        for i in range(numData):
            value = float(serial_port.readline().strip())
            data[i].append(value)
            lines[i].set_data(range(Samples),data[i])
            print (data[0][-1], data[1][-1]) 
#Write data to .csv/.txt 
            outf.write(str(waktu)+";"+str(data[0][-1])+";"+str(data[1][-1])+"\n")
            canvas.draw() 

    root.after(1,plot_data)  

def plot_start(): 
    global cond 
    cond = True
    serial_port.reset_input_buffer() 

def plot_stop(): 
    global cond
    cond = False 

def plot_save():
    canvas.print_figure(str(nama_file)+'.png',format='png')  

#KODE GUI
root = tk.Tk()
root.title('Real Time Plot') 
root.configure(background = 'green')
root.geometry("600x480") 

#batas pada grafik
xmin = 0
xmax = Samples 
ymin = [0,0] 
ymax = [1023,1023] 
lines = [] 
data = []

for i in range(numData): 
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([], [], color='cyan')) #warna garis kurva

fig = Figure(); #membuat grafik data serial yang masuk
axl = fig.add_subplot(3, 1, 1,xlim=(xmin, xmax), ylim=(ymin[0], ymax[0])) 
axl.title.set_text('Plot Grafik Data-1')
axl.set_xlabel("Data")
axl.set_ylabel("Data Sensor")
axl.add_line(lines[0])

axl = fig.add_subplot(3, 1, 3,xlim=(xmin, xmax), ylim=(ymin[1], ymax[1])) 
axl.title.set_text('Plot Grafik Data-2')
axl.set_xlabel("Data")
axl.set_ylabel("Data Sensor")
axl.add_line(lines[1])



canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.get_tk_widget().place(x = 10,y=10, width = 540, height = 360) 
canvas.draw()

#membuat Tombol 
root.update();
start = tk.Button(root, text = "Start", font = ('calibri',12),command = lambda: plot_start(),bg="yellow")
start.place(x = 150, y = 420)

root.update();
stop = tk.Button(root, text = "Stop", font = ('calibri',12),command = lambda: plot_stop(),bg="yellow")
stop.place(x = start.winfo_x()+start.winfo_reqwidth() + 100, y = 420)

root.update();
save = tk.Button(root, text = "Save", font = ('calibri',12),command = lambda: plot_save(),bg="yellow")
save.place(x = start.winfo_x()+start.winfo_reqwidth() + 50, y = 420)

root.after(1,plot_data)
root.mainloop()
