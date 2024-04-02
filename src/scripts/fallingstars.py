import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Star:
    def __init__(self):
        self.x = random.uniform(-2.0, 2.0)
        self.y = random.uniform(-2.0, 2.0)
        self.z = random.uniform(-10.0, -1.0)
        self.speed = random.uniform(0.005, 0.02)
        self.size = random.uniform(0.005, 0.02)

    def update(self):
        self.z += self.speed
        if self.z > 0:
            self.x = random.uniform(-2.0, 2.0)
            self.y = random.uniform(-2.0, 2.0)
            self.z = random.uniform(-10.0, -1.0)
            self.speed = random.uniform(0.005, 0.02)
            self.size = random.uniform(0.005, 0.02)

def draw_star(star):
    glPointSize(star.size * 100)
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(star.x, star.y, star.z)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    for star in stars:
        draw_star(star)
        star.update()

    glutSwapBuffers()

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

stars = []

for _ in range(100):
    stars.append(Star())

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Estrelas Cadentes")
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (800/600), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glutDisplayFunc(draw)
glutTimerFunc(16, timer, 0)
glutMainLoop()
