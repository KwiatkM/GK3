import numpy as np
from light import Light
from material import Material, test1

class Sphere():

    def __init__(self) -> None:
        self.center = np.array([0,0,0])
        self.r = 1
        self.color = "#000000"
        self.material = test1


    def getAmbient(self, light):
        return light.i_a * self.material.k_a

    def getDiffuse(self, x, y, light:Light):
        n = self.getNormal(x,y)
        l = self.getVectorToLightN(n, light)
        return (light.i_d * self.material.k_d * np.dot(n,l)).clip(min=0)
    
    def getSpecular(self, x, y, light:Light):
        n = self.getNormal(x,y)
        l = -self.getVectorToLight(n, light)
        if(np.dot(-l, n) <=0 ): return np.array([0.0, 0.0, 0.0])
        r = l - 2 * (np.dot(l,n)) * n
        r = r / np.sqrt(np.dot(r,r))
        return (light.i_s * self.material.k_s * pow(np.dot(r,np.asarray([0,0,1])), self.material.n) ).clip(min=0)
        


    def getNormal(self, x, y):
        return np.array([x,y,np.sqrt(1 - (x*x) - (y*y))])
    
    def getVectorToLightN(self, point, light:Light):
        v = light.point - point
        vn = v / np.sqrt(np.dot(v,v))
        return  vn
    
    def getVectorToLight(self, point, light:Light):
        v = light.point - point
        return  v