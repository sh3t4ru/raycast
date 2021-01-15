class Coordinate:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Ray:
    def __init__(self, point: Coordinate, vector: Coordinate):
        self.point = point
        self.vector = vector


class Figure:
    def __init__(self, center: Coordinate, color):
        self.center = center
        self.color = color


class Sphere(Figure):
    def __init__(self, center: Coordinate, color, radius: float):
        super().__init__(center, color)
        self.radius = radius

    def intersect(self, ray: Ray) -> (Coordinate, float):
        x0 = ray.point.x - self.center.x
        y0 = ray.point.y - self.center.y
        z0 = ray.point.z - self.center.z

        a = ray.vector.x ** 2 + ray.vector.y ** 2 + ray.vector.z ** 2
        b = 2 * (ray.vector.x * x0 + ray.vector.y * y0 + ray.vector.z * z0)
        c = x0 ** 2 + y0 ** 2 + z0 ** 2 - self.radius ** 2
        d = b ** 2 - 4 * a * c

        if d < 0:
            return None, float('inf')   # не попали

        t1 = (-b + d ** 0.5) / (2 * a)
        t2 = (-b - d ** 0.5) / (2 * a)

        p1 = Coordinate(ray.vector.x * t1 + ray.point.x,
                        ray.vector.y * t1 + ray.point.y,
                        ray.vector.z * t1 + ray.point.z)
        p2 = Coordinate(ray.vector.x * t2 + ray.point.x,
                        ray.vector.y * t2 + ray.point.y,
                        ray.vector.z * t2 + ray.point.z)

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
    def __init__(self, center: Coordinate, color, size: Coordinate):
        super().__init__(center, color)
        self.size = size

    def intersect(self, ray: Ray) -> (Coordinate, float):
        pass


def distance_between(p1: Coordinate, p2: Coordinate) -> float:
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2) ** 0.5


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
    lighter = Coordinate(300.0, 0.0, -300.0)
    distance = distance_between(impact, lighter)
    r, g, b = map(lambda x: min(255, max(0, int(x * (1 - (distance - 240.0) / 200.0)))), (r, g, b))
    color = '#' + '{:02x}'.format(r) + '{:02x}'.format(g) + '{:02x}'.format(b)
    return color
