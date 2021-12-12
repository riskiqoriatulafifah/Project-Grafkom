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

def timer(value):
    global x_body,game_over, kecepatan, fruit_position, score, score_add, speed_level, level, speed_timer
    if game_over == True:
        kecepatan = 0
        score_add = 0
        speed_level = 0
        score_add = 0 
        
    x_body += kecepatan
    score += kecepatan + score_add
    
    
    if x_body > 550 and y_body != fruit_position[1]:
        kecepatan = 0
        score_add = 0
        game_over = True
        
    elif x_body == 550 and y_body == fruit_position[1]:
        fruit_position = [550,y_fruit[random.randint(1,len(y_fruit))]]
        kecepatan = 10  
        x_body = 160
    
    if speed_timer > 50:
        if score%600== 0:
            speed_level += 20
            speed_timer -= speed_level
            level += 1
    else:
        speed_timer = 50
        speed_level = 0    
        
    glutTimerFunc(speed_timer,timer,0)


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
