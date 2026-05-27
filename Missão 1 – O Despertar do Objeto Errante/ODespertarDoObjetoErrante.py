from OpenGL.GL import *
from OpenGL.GLUT import *

#glTranslayef(x,y,z)

def pegarTecla(key, x, y):
    if key == b'w':
        glTranslatef(0, 0.1, 0)
        glutPostRedisplay()
    if key == b's':
        glTranslatef(0, -0.1, 0)
        glutPostRedisplay()
    if key == b'a':
        glTranslatef(-0.1, 0, 0)
        glutPostRedisplay()
    if key == b'd':
        glTranslatef(0.1, 0, 0)
        glutPostRedisplay()

def quadrado():
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glEnd()
    glFlush()
    glutSwapBuffers()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    quadrado()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b'O Despertar do Objeto Errante')
glutInitWindowSize(800, 600)
glutDisplayFunc(display)
glutKeyboardFunc(pegarTecla)
glutMainLoop()