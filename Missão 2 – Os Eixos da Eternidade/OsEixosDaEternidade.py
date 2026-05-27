from OpenGL.GL import *
from OpenGL.GLUT import *


def pegarTecla(key, x, y):

    if key == b'x':
        glRotatef(10, 1, 0, 0)
        glutPostRedisplay()
    if key == b'X':
        glRotatef(-10, 1, 0, 0)
        glutPostRedisplay()
    if key == b'y':
        glRotatef(10, 0, 1, 0)
        glutPostRedisplay()
    if key == b'Y':
        glRotatef(-10, 0, 1, 0)
        glutPostRedisplay()
    if key == b'z':
        glRotatef(10, 0, 0, 1)
        glutPostRedisplay()
    if key == b'Z':
        glRotatef(-10, 0, 0, 1)
        glutPostRedisplay()


def desenho():
    glutSolidTeapot(0.4)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    desenho()
    glFlush()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b'Os Eixos da Eternidade')
glutInitWindowSize(800, 600)
glutDisplayFunc(display)
glutKeyboardFunc(pegarTecla)
glutMainLoop()
