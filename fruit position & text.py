#import library
import random
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# BODY ULAR
x_body = 160
y_body = 150

# fruit position
y_fruit = []
for i in range(60,440):
	if i%10==0:
		y_fruit.append(i)
  
fruit_position = [550,y_fruit[random.randint(1,len(y_fruit))]]
game_over = False
#draw text
    
def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    
          
def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

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
    init()
    glutMainLoop()
