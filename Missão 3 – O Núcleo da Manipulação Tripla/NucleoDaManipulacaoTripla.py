from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from BonecoMine import BonecoMine
import sys


boneco = BonecoMine()

def configurar_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        0, 0, 6,
        0, 0, 0,
        0, 1, 0
    )

    
def pegar_tecla(key, x, y):
    if key == b't':
        glTranslatef(0.1, 0.0, 0.0)
        glutPostRedisplay()
    if key == b'T':
        glTranslatef(-0.1, 0.0, 0.0)
        glutPostRedisplay()
    if key == b'y':
        glRotatef(10, 0.0, 1.0, 0.0)
        glutPostRedisplay()
    if key == b'Y':
        glRotatef(-10, 0.0, 1.0, 0.0)
        glutPostRedisplay()
    if key == b'e':
        glScalef(1.1, 1.1, 1.1)
        glutPostRedisplay()
    if key == b'E':
        glScalef(0.9, 0.9, 0.9)
        glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    boneco.cabeca()
    boneco.braço_direito()
    boneco.braço_esquerdo()
    boneco.mao_direita()
    boneco.mao_esquerda()
    boneco.tronco()
    boneco.perna()
    boneco.sapato()
    glutSwapBuffers()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    configurar_camera()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Nucleo da Manipulacao Tripla")
init()
glutDisplayFunc(display)
glutKeyboardFunc(pegar_tecla)
glutMainLoop()
