from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Cubo: 

    def __init__(self):
        pass

    def draw(self):

        glPushMatrix()

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
            [0, 4, 5, 1],
            [0, 5, 6, 7],
            [0, 2, 6, 4],
            [2, 6, 7, 3],
            [1, 3, 7, 5]
        ]

        cores = [

        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
    ]

        glBegin(GL_QUADS)
        glColor3fv([0 ,1 ,1])
        for i, face in enumerate(faces):
            glColor3fv(cores[i])
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()
        glPopMatrix()