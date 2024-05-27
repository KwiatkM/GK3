from tkinter import Canvas
from sphere import Sphere
from light import Light
import numpy as np

P = 10
SPACE = 20 

class Scene():
    
    def __init__(self, canvas:Canvas,canvas_width, canvas_height, xlim, ylim) -> None:
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.xlim = xlim
        self.ylim = ylim
        self.z = 2
        self.sphere = Sphere()
        self.light = Light(np.array([6.0,-6.0, 6.0]))
        
 

    def render(self):
        self.canvas.delete("all")

        r = self.sphere.r
        c = self.sphere.color
        radiusDenormalized = int((self.sphere.r / self.xlim) * self.canvas_width)
        boundingBoxStartX = self.canvas_width/2 - radiusDenormalized
        boundingBoxStartY = self.canvas_height/2 - radiusDenormalized
        
        for y in range(2*radiusDenormalized):
            for x in range(2*radiusDenormalized):
                # xNorm, yNorm = (-1, 1)
                yNorm = (y/radiusDenormalized) -1
                xNorm = (x/radiusDenormalized) -1
                if r - xNorm*xNorm - yNorm*yNorm < 0:
                    continue
                
                ambientColor = self.sphere.getAmbient(self.light)
                diffuseColor = self.sphere.getDiffuse(xNorm, yNorm, self.light)
                specularColor = self.sphere.getSpecular(xNorm, yNorm, self.light)
                #d = self.sphere.getDiffuse(xNorm, yNorm, self.light)

                c = ambientColor + diffuseColor + specularColor


                c = c.clip(max=1)
                c = c * 255
                c = '#%02x%02x%02x' % (int(c[0]), int(c[1]), int(c[2]))
                self.canvas.create_line(boundingBoxStartX + x, boundingBoxStartY + y, boundingBoxStartX + x + 1, boundingBoxStartY + y, fill=c)

           
        
        self.ka = self.canvas.create_text(50,P + 0 * SPACE,text= "k_a = " + str(round(self.sphere.material.k_a, 2)) )
        self.kd = self.canvas.create_text(50,P + 1 * SPACE,text= "k_d = " + str(round(self.sphere.material.k_d, 2)) )
        self.ks = self.canvas.create_text(50,P + 2 * SPACE,text= "k_s = " + str(round(self.sphere.material.k_s, 2)) )
        self.n =  self.canvas.create_text(50,P + 3 * SPACE,text= "n = " + str(round(self.sphere.material.n, 2)) )
        self.drawPos()


    def drawPos(self):
        self.lightPos = self.canvas.create_text(60,P + 4 * SPACE,text= "light = [" + 
                                           str(round(self.light.point[0], 2)) + ", " +
                                           str(round(-self.light.point[1], 2)) + ", " + 
                                           str(round(self.light.point[2], 2)) + "]")


    def k_a_up(self):
        self.canvas.delete(self.ka)
        self.sphere.material.k_a += 0.05
        self.ka = self.canvas.create_text(50,P + 0 * SPACE,text= "k_a = " + str(round(self.sphere.material.k_a, 2)) )
    
    def k_a_down(self):
        self.canvas.delete(self.ka)
        self.sphere.material.k_a -= 0.05
        self.ka = self.canvas.create_text(50,P + 0 * SPACE,text= "k_a = " + str(round(self.sphere.material.k_a, 2)) )

    def k_d_up(self):
        self.canvas.delete(self.kd)
        self.sphere.material.k_d += 0.05
        self.kd = self.canvas.create_text(50,P + 1 * SPACE,text= "k_d = " + str(round(self.sphere.material.k_d, 2)) )
    
    def k_d_down(self):
        self.canvas.delete(self.kd)
        self.sphere.material.k_d -= 0.05
        self.kd = self.canvas.create_text(50,P + 1 * SPACE,text= "k_d = " + str(round(self.sphere.material.k_d, 2)) )
            
    def k_s_up(self):
        self.canvas.delete(self.ks)
        self.sphere.material.k_s += 0.05
        self.ks = self.canvas.create_text(50,P + 2 * SPACE,text= "k_s = " + str(round(self.sphere.material.k_s, 2)) )
    
    def k_s_down(self):
        self.canvas.delete(self.ks)
        self.sphere.material.k_s -= 0.05
        self.ks = self.canvas.create_text(50,P + 2 * SPACE,text= "k_s = " + str(round(self.sphere.material.k_s, 2)) )

    def n_up(self):
        self.canvas.delete(self.n)
        self.sphere.material.n += 2
        self.n = self.canvas.create_text(50,P + 3 * SPACE,text= "n = " + str(round(self.sphere.material.n, 2)) )
    
    def n_down(self):
        self.canvas.delete(self.n)
        self.sphere.material.n -= 2
        self.n = self.canvas.create_text(50,P + 3 * SPACE,text= "n = " + str(round(self.sphere.material.n, 2)) )

    # light 

    def x_up(self):
        self.canvas.delete(self.lightPos)
        self.light.point[0] -= 0.5
        self.drawPos()
    
    def x_down(self):
        self.canvas.delete(self.lightPos)
        self.light.point[0] += 0.5
        self.drawPos()

    def y_up(self):
        self.canvas.delete(self.lightPos)
        self.light.point[1] += 0.5
        self.drawPos()
    
    def y_down(self):
        self.canvas.delete(self.lightPos)
        self.light.point[1] -= 0.5
        self.drawPos()
    
    def z_up(self):
        self.canvas.delete(self.lightPos)
        self.light.point[2] += 0.5
        self.drawPos()
    
    def z_down(self):
        self.canvas.delete(self.lightPos)
        self.light.point[2] -= 0.5
        self.drawPos()

