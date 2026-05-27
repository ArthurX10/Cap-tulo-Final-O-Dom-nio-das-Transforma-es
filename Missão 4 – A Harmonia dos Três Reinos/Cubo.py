from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Cubo: 

    def __init__(self):
        pass

    def draw(self):

        glPushMatrix()

        glTranslatef(-1.3, 0, 0)

        
        vertices = [
            [0.5, 0.5, 0.5],
            [0.5, 0.5, -0.5],
            [0.5, -0.5, 0.5],
            [0.5, -0.5, -0.5],
            [-0.5, 0.5, 0.5],
            [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5],
            [-0.5, -0.5, -0.5]
        ]

        faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 4, 5, 1],
            [2, 6, 7, 3],
            [0, 2, 6, 4],
            [1, 3, 7, 5]
        ]

        glBegin(GL_QUADS)
        glColor3fv([1 ,0 ,0])
        for i, face in enumerate(faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()
        glPopMatrix()