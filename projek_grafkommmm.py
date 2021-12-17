#import library
import random
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = 0 # FOR TRANSLATE
kecepatan = 10
score = 0
score_add = 2
speed_level = 0
speed_timer = 200
level = 1
# BODY ULAR
x_body = 160
y_body = 150

# fruit position
y_fruit = []
for i in range(60,441):
	if i%10==0:
		y_fruit.append(i)
x_fruit = []
for i in range(380,551):
	if i%10==0:
		x_fruit.append(i)
  
fruit_position = [x_fruit[random.randint(0,len(x_fruit)-1)],y_fruit[random.randint(0,len(y_fruit)-1)]]
fruit_position2 = [x_fruit[random.randint(0,len(x_fruit)-1)],y_fruit[random.randint(0,len(y_fruit)-1)]]
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

def makanan(x,y):
    glPushMatrix()
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(255,251,0)
    glVertex2f(x,y)
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

def input_keyboard(key,x,y):
    global y_body
    if key == GLUT_KEY_UP:
        if y_body == 440:
            y_body +=0
        else:
            y_body += 10
            
    elif key == GLUT_KEY_DOWN:
        if y_body == 60:
            y_body -=0
        else:
            y_body -= 10
        
#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if game_over == False:
        bg()
        ular(x_body)
        makanan(fruit_position[0],fruit_position[1])
        makanan(fruit_position2[0],fruit_position2[1])
        drawText("YOUR LEVEL: ", 20,460,0,0,0)
        drawTextNum(level,130,460,0,0,0)
        drawText("YOUR SCORE: ", 20,430,0,0,0)
        drawTextNum(score,20,400,0,0,0)
    else:
        bg()
        drawText("G A M E O V E R   ", 280,300,0,0,0)
        drawText("YOUR LEVEL : ", 200,270,0,0,0)
        drawTextNum(level,350,270,0,0,0)
        drawText("YOUR SCORE : ", 200,250,0,0,0)
        drawTextNum(score,350,250,0,0,0)
        
    glutSwapBuffers()

def init():
    glClearColor(2,1,0, 2.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def timer(value):
    global x_body,game_over, kecepatan, fruit_position, fruit_position2, score, score_add, speed_level, level, speed_timer
    x_body += kecepatan
    score += kecepatan + score_add
    
    if game_over == True:
        kecepatan = 0
        score_add = 0
        speed_level = 0
        score_add = 0     
    
    else:
        if x_body > 550  and ((y_body != fruit_position[1]) or (y_body != fruit_position2[1])):
            kecepatan = 0
            score_add = 0
            game_over = True
            
        elif ((x_body == fruit_position[0]) and (y_body == fruit_position[1])):
            x_body = 160
            kecepatan = 10  
            fruit_position = [x_fruit[random.randint(0,len(x_fruit)-1)],y_fruit[random.randint(0,len(y_fruit)-1)]]
            fruit_position2 = [x_fruit[random.randint(0,len(x_fruit)-1)],y_fruit[random.randint(0,len(y_fruit)-1)]]

            
        elif ((x_body == fruit_position2[0]) and (y_body == fruit_position2[1])):        
            x_body = 160
            kecepatan = 10  
            fruit_position = [x_fruit[random.randint(0,len(x_fruit)-1)],y_fruit[random.randint(0,len(y_fruit)-1)]]
            fruit_position2 = [x_fruit[random.randint(0,len(x_fruit)-1)],y_fruit[random.randint(0,len(y_fruit)-1)]]

        if speed_timer > 50:
            if score%600== 0:
                speed_level += 20
                speed_timer -= speed_level
                level += 1
        else:
            speed_timer = 50
            speed_level = 0    
    glutTimerFunc(speed_timer,timer,0)

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

main()