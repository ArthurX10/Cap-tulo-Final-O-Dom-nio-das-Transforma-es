from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Figura import Figura

cruz = Figura()

escala_x = 1
escala_y = 1

def pegar_tecla(key, x, y):
    global escala_x, escala_y
    if key == b'x':
        escala_y = -escala_y
        glutPostRedisplay()
    elif key == b'y':
        escala_x = -escala_x
        glutPostRedisplay()

def desenharEixos():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex2f(-5, 0)
    glVertex2f(5, 0)
    

    glColor3f(0, 1, 0)
    glVertex2f(0, -5)
    glVertex2f(0, 5)
    
    glEnd()
    glLineWidth(1.0)


def display():  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    desenharEixos()

    glPushMatrix()
    glScalef(escala_x, escala_y, 1)
    cruz.draw()
    glPopMatrix()
    glutSwapBuffers()

def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b'O Encontro das Sombras')
glutReshapeWindow(800, 800)
glutDisplayFunc(display)
glutKeyboardFunc(pegar_tecla)
init()
glutMainLoop()
