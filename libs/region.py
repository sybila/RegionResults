class Region():
    def __init__(self, area, sat):
        self.area = area
        self.sat = sat

    def projection(self, param):
        return self.area[param]

    def __str__(self):
        return str(self.area) + " " + str(self.sat)


def get_bounds(regions, x, y):
    x_max = max(list(map(lambda result: result.projection(x)[1], regions)))
    y_max = max(list(map(lambda result: result.projection(y)[1], regions)))

    x_min = min(list(map(lambda result: result.projection(x)[0], regions)))
    y_min = min(list(map(lambda result: result.projection(y)[0], regions)))

    return {"x_min": x_min, "x_max": x_max, "y_min": y_min, "y_max": y_max}