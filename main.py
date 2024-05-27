import tkinter as tk
from scene import Scene
from light import Light
import numpy as np

WIDTH = 700
HEIGHT = 700

window  = tk.Tk()
window.geometry("" + str(WIDTH) + "x" + str(HEIGHT))

canvas = tk.Canvas(window, bg='grey90', width=WIDTH, height=HEIGHT)
canvas.pack()

scene = Scene(canvas, WIDTH, HEIGHT, 8,8)

scene.render()


def k_a_up(event): 
    scene.k_a_up()

def k_a_down(event):
    scene.k_a_down()

def k_d_up(event): 
    scene.k_d_up()

def k_d_down(event):
    scene.k_d_down()

def k_s_up(event): 
    scene.k_s_up()

def k_s_down(event):
    scene.k_s_down()

def n_up(event): 
    scene.n_up()

def n_down(event):
    scene.n_down()

def x_up(event):
    scene.x_up()

def x_down(event):
    scene.x_down()

def y_up(event):
    scene.y_up()

def y_down(event):
    scene.y_down()

def z_up(event):
    scene.z_up()

def z_down(event):
    scene.z_down()

def redraw(event):
    scene.render()


window.bind('a', k_a_up)
window.bind('z', k_a_down)
window.bind('s', k_d_up)
window.bind('x', k_d_down)
window.bind('d', k_s_up)
window.bind('c', k_s_down)
window.bind('f', n_up)
window.bind('v', n_down)

window.bind('<Left>', x_up)
window.bind('<Right>', x_down)
window.bind('<Down>', y_up)
window.bind('<Up>', y_down)
window.bind('o', z_up)
window.bind('l', z_down)

window.bind('<Return>', redraw)



window.mainloop()