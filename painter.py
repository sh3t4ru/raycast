from tkinter import Tk, Frame, BOTH, Canvas
from rayengine import *
import time


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Sphere")
        self.pack(fill=BOTH, expand=1)

        s1 = Sphere(Coordinate(100.0, 100.0, 50.0), "#aa50bb", 40.0)
        s2 = Sphere(Coordinate(140.0, 140.0, 40.0), "#ffa500", 40.0)
        s3 = Sphere(Coordinate(100.0, 70.0, 40.0), "#20b2aa", 20.0)
        s4 = Sphere(Coordinate(120.0, 100.0, 38.0), "#696969", 29.0)

        canvas = Canvas(self)

#        start_time = time.time()

        for x in range(0, 200):
            for y in range(0, 200):
                ray = Ray(Coordinate(100.0, 100.0, -800.0), Coordinate(x - 100.0, y - 100.0, 800.0))
                color = cast_ray(ray, [s1, s2, s3, s4])
        #        color = cast_ray(ray, [s1])
                canvas.create_line(x, y, x + 1, y + 1, fill=color)

 #       print(time.time() - start_time)

        canvas.pack(fill=BOTH, expand=1)


def main():
    height = 200
    weight = 200

    root = Tk()
    root.geometry(str(weight) + "x" + str(height) + "+300+300")
    app = Example(root)
    root.mainloop()


main()
