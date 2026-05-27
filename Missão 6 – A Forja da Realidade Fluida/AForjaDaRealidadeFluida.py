from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Cubo import Cubo
import numpy as np
import sys

cubo = Cubo()

sh = 0

def configurar_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, 1, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        4, 3, 6,
        0, 0, 0,
        0, 1, 0
    )

def Pegar_tecla(key, x, y):
    if key == b'h': 
        global sh
        sh += 0.1
        glutPostRedisplay()
    elif key == b'H':
        sh -= 0.1
        glutPostRedisplay()
        pass
    elif key == b'z':
        sh = 0
        glutPostRedisplay()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    configurar_camera()

    glPushMatrix()
    
    shear = np.array([
     1, sh, 0 , 0,
     0, 1, 0, 0, 
     0, 0, 1, 0,
     0, 0, 0, 1
    ], dtype=np.float32)
    glMultMatrixf(shear)

    cubo.draw()
    glPopMatrix()

    glutSwapBuffers()

def init():
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)



glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"A Forja da Realidade Fluida")
init()
glutDisplayFunc(display)
glutKeyboardFunc(Pegar_tecla)
glutMainLoop()



