from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Car:
    def __init__(self) -> None:
        self.points = [(1.0, 1.0), (1.0, 3.0), (3.0, 3.3), (1.0, 3.5), (3.5, 3.5)]

    def draw(self):
        glBegin(GL_LINE_LOOP)
        glColor(1.0, 1.0, 1.0)
        for i in self.points:
            glVertex2d(i[0], i[1])
        glEnd()


class App:
    def __init__(self) -> None:
        self.car = Car()

    def run(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPushMatrix()
        glScale(0.1, 0.1, 0.1)
        self.car.draw()
        glPopMatrix()
        glFlush() 

if __name__ == "__main__":
    app = App()
    glutInit(argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(200, 200)
    glutCreateWindow("Game")
    glutDisplayFunc(app.run)
    glutMainLoop()