from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_QUADS


class Dino:
    def __init__(self) -> None:
        self.x = 0
        self.points = [(1.0,3.0), (1.9,1.4), (2.9,0.8), (3.0,0.0), (3.7, 0), (3.4,0.3), (3.4,0.8), (4.0,1.1), (4.4,1.8), (4.5,2.3), (4.9,2.3), (5.2,2.0), (5.3,2.1), (4.9,2.6), (4.5,2.6), (4.7,3.2), (5.1,3.1), (5.3,3.3), (4.8,3.5), (5.5,3.5), (5.3,3.9), (4.3,4.1), (3.7,3.9), (3.7,3.3), (3.4,2.6), (2.096,2.3)]
        self.points.reverse()

    def draw(self):
        glBegin(GL_LINE_LOOP)
        glColor(1.0, 1.0, 1.0)
        for i in self.points:
            glVertex2d(i[0], i[1])
        glEnd()


class App:
    def __init__(self) -> None:
        self.dino = Dino()

    def run(self):
        self.dino.x += 1
        glClear(GL_COLOR_BUFFER_BIT)
        glPushMatrix()
        glScale(0.1, 0.1, 0.1)
        glTranslate(-5, 0, 0)
        self.dino.draw()
        glPopMatrix()
        glFlush()

if __name__ == "__main__":
    app = App()
    glutInit(argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Game")
    glutDisplayFunc(app.run)
    glutMainLoop()