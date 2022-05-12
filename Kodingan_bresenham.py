# Nama  : Muhammad Ramadhan Muna
# NIM   : 20051397059
# Kelas : D4 Manajemen Informatika - 2020A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-50.0, 50.0, -50.0, 50.0)
    glPointSize(5)


def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def bresenham_drawing_circle(r):

    # lokasi lingkaran hasil output
    x_center = -10
    y_center = 10

    r = 9
    x = 0
    y = r

    # parameter keputusan
    d = 3 - 2 * r

    # membuat titik koordinat yang ditentukan
    plot(x + x_center, y + y_center)

    while y > x:

        if d < 0:
            x += 1
            d += 4 * x + 6
        else:
            x += 1
            y -= 1
            d += (4 * (x - y)) + 10

    # mencari nilai (x, y)
    # membalikkan nilai menjadi (y, x)

        #nilai (x, y)
        # kuadran 1
        plot(x + x_center, y + y_center)

        # kuadran 2
        plot(x + x_center, -y + y_center)

        # kuadran 3
        plot(-x + x_center, -y + y_center)

        # kuadran 4
        plot(-x + x_center, y + y_center)

        #nilai (y, x)
        # kuadran 1
        plot(y + x_center, x + y_center)

        # kuadran 2
        plot(-y + x_center, x + y_center)

        # kuadran 3
        plot(-y + x_center, -x + y_center)

        # kuadran 4
        plot(y + x_center, -x + y_center)


def plotpoints():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1.0, 1.0)

    glBegin(GL_LINES)

    glEnd()

    bresenham_drawing_circle(40)

    glFlush()


# menampilkan hasil output
def main():
    # inisialisasi glut
    glutInit(sys.argv)
    # inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # inisialisasi ukuran layar glut
    glutInitWindowSize(500, 500)
    # inisiasliasi posisi layar glut
    glutInitWindowPosition(100, 100)
    # inisialisasi pembuatan window
    glutCreateWindow("Tugas Praktikum Bresenham")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()


main()
