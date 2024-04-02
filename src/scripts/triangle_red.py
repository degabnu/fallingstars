from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configura a matriz de projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800/600), 0.1, 100.0)  # Defina o campo de visão, aspect ratio, plano próximo e plano distante
    
    # Configura a matriz de modelo-visão
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)  # Define a posição da câmera, o ponto para onde ela está olhando e a orientação da câmera
    
    # Desenha o triângulo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Vermelho
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()

    glutSwapBuffers()

# Inicializa o GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"OpenGL Window")
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(draw)
glutMainLoop()
