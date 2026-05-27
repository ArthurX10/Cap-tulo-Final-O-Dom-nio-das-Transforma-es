from OpenGL.GL import *
from OpenGL.GLUT import *


class BonecoMine:

    def __init__(self):
        self.faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [0, 3, 7, 4],
            [1, 2, 6, 5]
        ]

    def cabeca(self):
        vertices = [
            (-0.3, 1.3, 1),
            ( 0.3, 1.3, 1),
            ( 0.3, 1.3, 0.5),
            (-0.3, 1.3, 0.5),

            (-0.3, 0.8, 1),
            ( 0.3, 0.8, 1),
            ( 0.3, 0.8, 0.5),
            (-0.3, 0.8, 0.5),
        ]

        glBegin(GL_QUADS)
        glColor3fv([1.0, 0.8, 0.6])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    def braço_direito(self):
        vertices = [
            (-0.3, 0.8, 1),
            (-0.8, 0.8, 1),
            (-0.8, 0.4, 1),
            (-0.3, 0.4, 1),
            (-0.3, 0.8, 0.5),
            (-0.8, 0.8, 0.5),
            (-0.8, 0.4, 0.5),
            (-0.3, 0.4, 0.5),
        ]

        glBegin(GL_QUADS)
        glColor3fv([0.5, 0.8, 1])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    def braço_esquerdo(self):
        vertices = [
            (0.3, 0.8, 1),
            (0.8, 0.8, 1),
            (0.8, 0.4, 1),
            (0.3, 0.4, 1),
            (0.3, 0.8, 0.5),
            (0.8, 0.8, 0.5),
            (0.8, 0.4, 0.5),
            (0.3, 0.4, 0.5),
        ]

        glBegin(GL_QUADS)
        glColor3fv([0.5, 0.8, 1])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    def mao_direita(self):
        vertices = [
            (0.3, 0.4, 1),
            (0.8, 0.4, 1),
            (0.8, -0.2, 1),
            (0.3, -0.2, 1),
            (0.3, 0.4, 0.5),
            (0.8, 0.4, 0.5),
            (0.8, -0.2, 0.5),
            (0.3, -0.2, 0.5),
        ]

        glBegin(GL_QUADS)
        glColor3fv([1, 0.8, 0.6])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    def mao_esquerda(self):
        vertices = [
            (-0.3, 0.4, 1),
            (-0.8, 0.4, 1),
            (-0.8, -0.2, 1),
            (-0.3, -0.2, 1),
            (-0.3, 0.4, 0.5),
            (-0.8, 0.4, 0.5),
            (-0.8, -0.2, 0.5),
            (-0.3, -0.2, 0.5),
        ]

        glBegin(GL_QUADS)
        glColor3fv([1, 0.8, 0.6])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    def tronco(self):
        vertices = [
            (-0.4, 0.8, 1),
            ( 0.4, 0.8, 1),
            ( 0.4, 0.8, 0.5),
            (-0.4, 0.8, 0.5),

            (-0.4, -0.4, 1),
            ( 0.4, -0.4, 1),
            ( 0.4, -0.4, 0.5),
            (-0.4, -0.4, 0.5),
        ]

        glBegin(GL_POLYGON)
        glColor3fv([0.5, 0.8, 1])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    def perna(self):
        vertices = [
            (-0.4, -0.4, 1),
            ( 0.4, -0.4, 1),
            ( 0.4, -0.4, 0.5),
            (-0.4, -0.4, 0.5),

            (-0.4, -1.4, 1),
            ( 0.4, -1.4, 1),
            ( 0.4, -1.4, 0.5),
            (-0.4, -1.4, 0.5),
        ]

        glBegin(GL_POLYGON)
        glColor3fv([0, 0, 0.3])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    def sapato(self):
        vertices = [
            (-0.4, -1.4, 1),
            ( 0.4, -1.4, 1),
            ( 0.4, -1.4, 0.5),
            (-0.4, -1.4, 0.5),

            (-0.4, -1.6, 1),
            ( 0.4, -1.6, 1),
            ( 0.4, -1.6, 0.5),
            (-0.4, -1.6, 0.5),
        ]
        glBegin(GL_POLYGON)
        glColor3fv([0, 0, 0.5])
        for i, face in enumerate(self.faces):
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()