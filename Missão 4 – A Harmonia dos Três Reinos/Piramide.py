from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



class Piramide:
    def __init__(self):
        pass

    
    def draw(self):

        vertices = [
            [0.5, 0.5, 0.5],
            [-0.5, -0.5, 0.5],
            [-0.5, 0.5, -0.5],
            [0.5, -0.5, -0.5]
        ]

        faces = [
            [0, 1, 2],
            [0, 1, 3],
            [0, 2, 3],
            [1, 2, 3]
        ]

        cores = [0, 0, 1]
        
        glColor3fv(cores)
        glBegin(GL_TRIANGLES)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()