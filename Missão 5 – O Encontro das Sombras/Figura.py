from OpenGL.GL import *
from OpenGL.GLUT import *




class Figura: 
    def __init__(self):
        pass

    def draw(self):
        glColor3f(0, 0, 1)
        glBegin(GL_TRIANGLES)
        glVertex2f(0.2, 0.6)
        glVertex2f(0.55, 0.6)
        glVertex2f(0.55, 0.2)
        glEnd()

        glColor3f(1, 0, 0)
        glBegin(GL_TRIANGLES)
        glVertex2f(0.9, 0.6)
        glVertex2f(0.55, 0.6)
        glVertex2f(0.55, 0.2)
        glEnd()


        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex(0.2, 0.7)
        glVertex(0.9, 0.7)
        glVertex(0.9, 0.6)
        glVertex(0.2, 0.6)
        


        glEnd()
        glFlush()
    

