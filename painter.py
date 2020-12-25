from tkinter import Tk, Frame, BOTH, Canvas
from rayengine import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Sphere")
        self.pack(fill=BOTH, expand=1)

        s1 = Sphere(Coordinate(100.0, 100.0, 50.0), "red", 40.0)
        s2 = Sphere(Coordinate(130.0, 160.0, 40.0), "orange", 30.0)
        s3 = Sphere(Coordinate(100.0, 70.0, 40.0), "blue", 20.0)
        s4 = Sphere(Coordinate(120.0, 100.0, 30.0), "black", 25.0)


        canvas = Canvas(self)
        for x in range(0, 300):
            for y in range(0, 200):
                ray = Ray(Coordinate(150.0, 100.0, -50.0), Coordinate(x - 150.0, y - 100.0, 100.0))
                color = cast_ray(ray, [s1, s2, s3, s4])
                canvas.create_line(x, y, x + 1, y + 1, fill=color)

        canvas.pack(fill=BOTH, expand=1)

def main():
    height = 200
    weight = 300

    root = Tk()
    root.geometry(str(weight) + "x" + str(height) + "+300+300")
    app = Example(root)
    root.mainloop()


main()
