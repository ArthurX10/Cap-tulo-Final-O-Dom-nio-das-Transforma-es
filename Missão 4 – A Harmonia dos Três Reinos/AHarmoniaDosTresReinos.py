from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
from Cubo import Cubo
from Piramide import Piramide
from sphere import Sphere

cubo = Cubo()
sphere = Sphere(0.5, 32, 32)
piramide = Piramide()

escala_cubo = 1.0
escala_piramide = 1.0
escala_sphere = 1.0

def Pegar_tecla(key, x, y):
    global escala_cubo, escala_piramide, escala_sphere, objeto

    if key == b'1':
        objeto = 1
    elif key == b'2':
        objeto = 2
    elif key == b'3':
        objeto = 3

    if key == b'+':
        if objeto == 1:
            escala_cubo += 0.1
            glutPostRedisplay()
        elif objeto == 2:
            escala_piramide += 0.1
            glutPostRedisplay()
        elif objeto == 3:
            escala_sphere += 0.1
            glutPostRedisplay()
    elif key == b'-':
        if objeto == 1:
            escala_cubo -= 0.1
            glutPostRedisplay()
        elif objeto == 2:
            escala_piramide -= 0.1
            glutPostRedisplay()
        elif objeto == 3:
            escala_sphere -= 0.1
            glutPostRedisplay()

   

def configurar_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        0, 5, 6,
        0, 0, 0,
        0, 1, 0
    )


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    

    glPushMatrix()
    glScalef(escala_cubo, escala_cubo, escala_cubo)
    cubo.draw()
    glPopMatrix()
    

    glPushMatrix()
    glScalef(escala_piramide, escala_piramide, escala_piramide)
    piramide.draw()
    glPopMatrix()

    glPushMatrix()
    glScalef(escala_sphere, escala_sphere, escala_sphere)
    sphere.draw()
    glPopMatrix()

    glutSwapBuffers()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    configurar_camera()
   



glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"A Harmonia dos Tres Reinos")
init()
glutDisplayFunc(display)
glutKeyboardFunc(Pegar_tecla)
glutMainLoop()
