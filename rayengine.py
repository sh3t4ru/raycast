class Coordinate:
    def __init__(self, x: float, y: float, z: float):
        self[0] = x
        self[1] = y
        self[2] = z


class Ray:
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector


class Figure:
    def __init__(self, center, color):
        self.center = center
        self.color = color


class Sphere(Figure):
    def __init__(self, center, color, radius: float):
        super().__init__(center, color)
        self.radius = radius

    def intersect(self, ray: Ray) -> (Coordinate, float):
        x0 = ray.point[0] - self.center[0]
        y0 = ray.point[1] - self.center[1]
        z0 = ray.point[2] - self.center[2]

        a = ray.vector[0] ** 2 + ray.vector[1] ** 2 + ray.vector[2] ** 2
        b = 2 * (ray.vector[0] * x0 + ray.vector[1] * y0 + ray.vector[2] * z0)
        c = x0 ** 2 + y0 ** 2 + z0 ** 2 - self.radius ** 2
        d = b ** 2 - 4 * a * c

        if d < 0:
            return None, float('inf')   # не попали

        t1 = (-b + d ** 0.5) / (2 * a)
        t2 = (-b - d ** 0.5) / (2 * a)

        p1 = (ray.vector[0] * t1 + ray.point[0],
              ray.vector[1] * t1 + ray.point[1],
              ray.vector[2] * t1 + ray.point[2])
        p2 = (ray.vector[0] * t2 + ray.point[0],
              ray.vector[1] * t2 + ray.point[1],
              ray.vector[2] * t2 + ray.point[2])

        dist1 = distance_between(ray.point, p1)
        dist2 = distance_between(ray.point, p2)

        if (t1 < 0) and (t2 < 0):
            return None, float('inf')  # вектор идёт в против. сторону если параметр отрицателен
        elif t1 < 0:
            return p2, dist2
        elif t2 < 0:
            return p1, dist1

        if dist1 < dist2:
            return p1, dist1
        else:
            return p2, dist2


class Rectangle(Figure):
    def __init__(self, center, color, size):
        super().__init__(center, color)
        self.size = size

    def intersect(self, ray: Ray) -> (Coordinate, float):
        pass


def distance_between(p1, p2) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5


def cast_ray(ray: Ray, shapes: list) -> str:
    distance = float('+inf')
    impact = None
    shape = None
    for cur_shape in shapes:
        (cur_impact, cur_distance) = cur_shape.intersect(ray)  # ОБРАБОТАТЬ НЕПОПАДАНИЕ (+inf если не попали)
        if cur_distance < distance:
            distance = cur_distance
            impact = cur_impact
            shape = cur_shape

    color = "#FFFFFF"
    if shape is not None:
        color = get_color(shape.color, impact, distance)

    return color


def get_color(color, impact, distance):
    r, g, b = map(lambda x: int(x, 16), (color[1: 3], color[3: 5], color[5: 7]))
    lighter = (300.0, 0.0, -300.0)
    distance = distance_between(impact, lighter)
    r, g, b = map(lambda x: min(255, max(0, int(x * (1 - (distance - 240.0) / 200.0)))), (r, g, b))
    color = '#' + '{:02x}'.format(r) + '{:02x}'.format(g) + '{:02x}'.format(b)
    return color
