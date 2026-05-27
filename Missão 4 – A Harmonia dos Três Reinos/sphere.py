from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np 

 
class Sphere:

    def __init__(self, radius, slices, stacks):
        self.radius = radius
        self.slices = slices
        self.stacks = stacks

    def draw(self):
        
        
        glPushMatrix()

        glTranslatef(1.3, 0, 0)

        glRotatef(90, 1, 0, 0)
       

        for i in range(self.stacks):
            lat0 = np.pi * (-0.5 + float(i) / self.stacks)
            z0 = self.radius * np.sin(lat0)
            zr0 = self.radius * np.cos(lat0)

            lat1 = np.pi * (-0.5 + float(i + 1) / self.stacks)
            z1 = self.radius * np.sin(lat1)
            zr1 = self.radius * np.cos(lat1)

            
            glBegin(GL_QUAD_STRIP)
            for j in range(self.slices + 1):
                lng = 2 * np.pi * float(j) / self.slices 
                x = np.cos(lng)
                y = np.sin(lng)
                glColor3fv((i / self.stacks, j / self.stacks, 1 - (i / self.stacks)))
                glVertex3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr1, y * zr1, z1)
            glEnd()
        glPopMatrix()


# tem que chamar ela na função principal e passar os valores de raio, slices e stacks