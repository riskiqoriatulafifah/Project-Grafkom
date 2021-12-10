#import library
import random
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def makanan():
    glPushMatrix()
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(255,251,0)
    glVertex2f(fruit_position[0],fruit_position[1])
    glEnd()
    glPopMatrix()

# PAGAR
def bg():
    x = 60
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(208,0,255)
    glVertex2f(130, 50)
    glVertex2f(500+x, 50)
    glVertex2f(500+x, 450)
    glVertex2f(130, 450)
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(130, 50)
    glVertex2f(499+x, 50)
    glVertex2f(499+x, 450)
    glVertex2f(130, 450)
    glEnd()
    glPopMatrix()

def init():
    glClearColor(2,1,0, 2.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)


def main ():   
    glutInit() 
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA) 
    glutInitWindowSize(600, 500) 
    glutInitWindowPosition(100,100) 
    glutCreateWindow("2D Snack Game")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen) 
    glutSpecialFunc(input_keyboard)
    timer(0)
    init()
    glutMainLoop()
