#import library
import random
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# BODY ULAR
x_body = 160
y_body = 150

def ular(x_body):
    glPushMatrix()
    glTranslate(x,0,0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(0,0,0)
    for i in range(4):
        glVertex2f(x_body,y_body)
        x_body-=10
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
