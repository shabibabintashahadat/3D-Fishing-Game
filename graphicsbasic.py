from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

# Basic text rendering function
def drawText(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(font, ord(character))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

# Basic OpenGL setup variables
WATER_LVL = 0
waveTime = 0
animSpeed = 0.05
